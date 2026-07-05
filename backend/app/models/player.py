from sqlmodel import SQLModel, Field, Relationship
from enum import Enum
from typing import Optional, List

class Sport(str, Enum):
    NFL = "NFL"
    NBA = "NBA"
    MLB = "MLB"
    NHL = "NHL"
    CFB = "CFB"

class ContestType(str, Enum):
    CLASSIC = "classic"
    TIERS = "tiers"
    SHOWDOWN = "showdown"

class EligiblePosition(str, Enum):
    # NFL / CFB
    QB = "QB"
    RB = "RB"
    WR = "WR"
    TE = "TE"
    FLEX = "FLEX"
    DST = "DST"
    CPT = "CPT"
    SUPER_FLEX = "Super FLEX"
    # MLB
    P = "P"
    C = "C"
    ONE_B = "1B"
    TWO_B = "2B"
    THREE_B = "3B"
    SS = "SS"
    OF = "OF"
    # NBA
    PG = "PG"
    SG = "SG"
    SF = "SF"
    PF = "PF"
    G = "G"
    F = "F"
    UTIL = "UTIL"
    # NHL
    W = "W"
    D = "D"
    # PGA
    GOLFER = "GOLFER"

class Player(SQLModel, table=True):
    __tablename__ = "player"
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    sport: Sport
    team: str
    real_position: str
    slates: List["PlayerSlate"] = Relationship(back_populates="player")

class PlayerSlate(SQLModel, table=True):
    __tablename__ = "player_slate"
    id: Optional[int] = Field(default=None, primary_key=True)
    player_id: Optional[int] = Field(default=None, foreign_key="player.id")
    site: str
    contest_type: ContestType
    salary: int
    projection: float
    slot_eligibility: List["PlayerSlotEligibility"] = Relationship(back_populates="player_slate")
    player: Optional["Player"] = Relationship(back_populates="slates")

class PlayerSlotEligibility(SQLModel, table=True):
    __tablename__ = "player_slot_eligibility"
    id: Optional[int] = Field(default=None, primary_key=True)
    player_slate_id: Optional[int] = Field(default=None, foreign_key="player_slate.id")
    slot: EligiblePosition
    player_slate: Optional["PlayerSlate"] = Relationship(back_populates="slot_eligibility")

