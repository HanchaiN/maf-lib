"""This module contains an implementation of a sort-orders.
"""
import abc
from functools import total_ordering

from maflib.util import abstractclassmethod


class SortOrder(object):
    """Base class for all sort orders.  Sub-classes should implement name and
    sortKey."""

    __metaclass__ = abc.ABCMeta

    def __init__(self, *args, **kwargs):
        pass

    @classmethod
    @abstractclassmethod
    def name(cls):
        """Returns the order's name."""

    @abc.abstractmethod
    def sort_key(self):
        """Function to generate the sort key for sorting records into this
        ordering"""

    @classmethod
    def all(cls):
        """Returns the known sort order classes."""
        return [
            BarcodeAndCoordinate
        ]

    @classmethod
    def find(cls, sort_order_name):
        """Returns the sort order class by name.  Throws an exception if
        none was found"""
        sort_order = next(iter([so for so in SortOrder.all()
                                if so.name() == sort_order_name]), None)
        if not sort_order:
            sort_orders = ", ".join([s.name() for s in SortOrder.all()])
            raise ValueError("Could not find sort order '%s', options: %s"
                             % (sort_order_name, sort_orders))
        return sort_order


@total_ordering
class SortOrderKey(object):
    """A container for the key used to sort MafRecords.  Sub-classes should
    implement the __cmp__ method."""

    __metaclass__ = abc.ABCMeta

    def __lt__(self, other):
        """Compare less than"""
        return self.__cmp__(other) < 0

    def __eq__(self, other):
        """Compare equal"""
        return self.__cmp__(other) == 0

    @abc.abstractmethod
    def __cmp__(self, other):
        """Compares two objects, returning -1 if this is less than the other, 0
        if they are equal, and 1 otherwise."""

    @classmethod
    def compare(cls, this, that):
        """Convenience method for comparing two objects of the same type that
        have a total ordering."""
        return (this > that) - (this < that)


class _BarcodesAndCoordinateKey(SortOrderKey):
    """A little class that aids in comparing records based on tumor barcode,
    matched normal barcode, chromosome, start position, and end position"""
    def __init__(self, record, contigs):
        self.tumor_barcode = record.value("Tumor_Sample_Barcode")
        self.normal_barcode = record.value("Matched_Norm_Sample_Barcode")
        self.chromosome = record.value("Chromosome")
        if contigs:
            try:
                self.chromosome = contigs.index(self.chromosome)
            except ValueError:
                raise ValueError(
                    "Could not find contig '%s' in list of contigs: %s"
                    % (self.chromosome, ", ".join(contigs))
                )
        self.start = record.value("Start_Position")
        self.end = record.value("End_Position")

    def __cmp__(self, other):
        diff = self.compare(self.tumor_barcode, other.tumor_barcode)
        if diff == 0:
            diff = self.compare(self.normal_barcode, other.normal_barcode)
        if diff == 0:
            diff = self.compare(self.chromosome, other.chromosome)
        if diff == 0:
            diff = self.compare(self.start, other.start)
        if diff == 0:
            diff = self.compare(self.end, other.end)
        return diff


class BarcodeAndCoordinate(SortOrder):
    """Defines a sort order based on the tumor barcode, matched normal
    barcode, chromosome, start position, and end position, in that order."""

    def __init__(self, fasta_index=None, *args, **kwargs):
        self._contigs = None
        if fasta_index:
            handle = open(fasta_index, "r")
            self._contigs = [line.rstrip("\r\n").split("\t")[0] for line in handle]
            handle.close()
        super(BarcodeAndCoordinate, self).__init__(*args, **kwargs)

    @classmethod
    def name(cls):
        """Returns the order's name."""
        return "BarcodesAndCoordinate"

    def sort_key(self):
        """Function to generate the sort key for sorting records into this
        ordering"""
        def key(record):
            """Gets the key"""
            return _BarcodesAndCoordinateKey(record=record,
                                             contigs=self._contigs)
        return key