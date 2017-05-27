"""
Stores the values for columns with custom types, typically stored in
Enumerations.
"""
from enum import Enum, unique

class MafEnum(Enum):
    """An enumeration that whose string representation is its value as a 
    string"""
    def __str__(self):
        return str(self.value)

@unique
class NullableYesOrNoEnum(MafEnum):
    """Enumeration for "Yes" or "No" column values, with Null being non-value"""
    Null = None
    No = "0"
    Yes = "1"


@unique
class NullableYOrNEnum(MafEnum):
    """Enumeration for "Y" or "N" column values, with Null being non-value"""
    Null = None
    No = "Y"
    Yes = "N"


@unique
class PickEnum(MafEnum):
    """Enumeration for the MAF 'Pick' column value"""
    Null = None
    Yes = "1"


@unique
class StrandEnum(MafEnum):
    """Enumeration for the MAF 'Strand' column value"""
    Plus = '+'
    Minus = '-'


@unique
class VariantClassificationEnum(MafEnum):
    """Enumeration for the MAF 'Variant_Classification' column value"""
    FrameShiftDeletion = "Frame_Shift_Del"
    FrameShiftInsertion = "Frame_Shift_Ins"
    InFrameInsertion = "In_Frame_Ins"
    InFrameDeletion = "In_Frame_Del"
    MissenseMutation = "Missense_Mutation"
    Nonsense_Mutation = "Nonsense_Mutation"
    Silent = "Silent"
    SpliceSite = "Splice_Site"
    Translation_Start_Site = "Translation_Start_Site"
    Nonstop_Mutation = "Nonstop_Mutation"
    ThreePrimerUtr = "3'UTR"
    ThreePrimeFlank = "3'Flank"
    FivePrimerUtr = "5'UTR"
    FivePrimeFlank = "5'Flank"
    IGR = "IGR"
    Intron = "Intron"
    RNA = "RNA"
    TargetedRegion = "Targeted_Region"
    SpliceRegion = "Splice_Region"


@unique
class VariantTypeEnum(MafEnum):
    """Enumeration for the MAF 'Variant_Type' column value"""
    SNP = "SNP"
    DNP = "DNP"
    TNP = "TNP"
    ONP = "ONP"
    INS = "INS"
    DEL = "DEL"
    Consolidated = "Consolidated"


@unique
class VerificationStatusEnum(MafEnum):
    """Enumeration for the MAF 'Verification_Status' column value"""
    Verified = "Verified"
    Unknown = "Unknown"


@unique
class MutationStatusEnum(MafEnum):
    """Enumeration for the MAF 'Mutation_Status' column value"""
    NoStatus = "None"
    Germline = "Germline"
    Somatic = "Somatic"
    LOH = "LOH"
    PostTranscriptional = "Post - transcriptional"
    Modification = "modification"
    Unknown = "Unknown"


@unique
class ValidationStatusEnum(MafEnum):
    """Enumeration for the MAF 'Validation_Status' column value"""
    Untested = "Untested"
    Inconclusive = "Inconclusive"
    Valid = "Valid"
    Invalid = "Invalid"


@unique
class SequencerEnum(MafEnum):
    """Enumeration for the MAF 'Sequencer' column value"""
    IlluminaGaII = "Illumina Genome Analyzer II"
    IllluminaGaIIx = "Illumina GAIIx"
    IlluminaHiSeq = "Illumina HiSeq"
    SOLID = "SOLID"
    FourFiveFour = "454"
    ABIThirtySevenThirty = "ABI 3730xl"
    IonTorrentPGM = "Ion Torrent PGM"
    IonTorrentProton = "Ion Torrent Proton"
    PacBioRS = "PacBio RS"
    IlluminaMiSeq = "Illumina MiSeq"
    IlluminaHiSeqTwoThousand = "Illumina HiSeq 2000"
    IlluminaHiSeqTwentyFiveHundred = "Illumina HiSeq 2500"
    FourFiveFourFLXTitanium = "454 GS FLX Titanium"
    ABOLiDFourSystem = "AB SOLiD 4 System"


@unique
class FeatureTypeEnum(MafEnum):
    """Enumeration for the MAF 'Feature_Type' column value"""
    Blank = ""
    Transcript = "Transcript"
    RegulatoryFeature = "RegulatoryFeature"
    MotifFeature = "MotifFeature"


@unique
class ImpactEnum(MafEnum):
    """Enumeration for the MAF 'Impact' column value"""
    Modifier = "MODIFIER"
    Low = "LOW"
    Moderate = "MODERATE"
    High = "HIGH"


@unique
class MC3OverlapEnum(MafEnum):
    """Enumeration for the MAF 'MC3_Overlap' column value"""
    Unknown = "Unknown"
    _True = "True"
    _False = "False"


@unique
class GdcValidationStatusEnum(MafEnum):
    """Enumeration for the MAF 'GDC_Validation_Status' column value"""
    Unknown = "Unknown"
    Valid = "Valid"
    Invalid = "Invalid"
    Inconclusive = "Inconclusive"