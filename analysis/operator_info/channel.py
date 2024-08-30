import copy
from sortedcontainers import SortedSet

import sigmond
from operator_info.isospin import Isospin

irreprows = {
    'A1': 1,
    'A2': 1,
    'E' : 2,
    'T1': 3,
    'T2': 3,
    'G1': 2,
    'G2': 2,
    'H' : 4,
    'B1': 1,
    'B2': 1,
    'G' : 2,
    'F1': 1,
    'F2': 1,
}


class Channel:

  EXTRA_INFO_KEYS = ['irrep', 'irreprow', 'momentum', 'momentum_squared', 'ref_momentum']

  def __init__(self, flavor, **extra_info):
    """Channel __init__ method

    Args:
      flavor (list[str]): the flavor of the channel
      **irrep (str): the irrep for the channel. If missing, it
          is assumed to be 'NONE'
      **irreprow (int): the irrep row for the channel. If missing, it
          is assumed that there is only one irrep row or the irrep row
          has been averaged over.
      **momentum (tuple of 3 ints): the definite momentum for
          a channel.
      **momentum_squared (int): the momentum squared for the channel,
          which assumes the equivalent momentum frames have been
          averaged over. Note that a momentum squared of 0 is treated
          as a momentum channel with P = (0, 0, 0)
      **ref_momentum (bool): specifies whether the momentum is ref.
          If missing, assumed to be False

    TODO:
      - Make use of sigmondbind.Momentum ?
    """

    self.flavor = flavor

    for attr, value in extra_info.items():
      if attr not in self.EXTRA_INFO_KEYS:
        logging.error(f"Unrecognized key {attr} in Channel")

      setattr(self, attr, value)

    if not hasattr(self, 'irrep'):
      self.irrep = 'NONE'

    if not hasattr(self, 'irreprow'):
      self.irreprow = 0

    if not hasattr(self, 'ref_momentum'):
      self.ref_momentum = False

    if hasattr(self, 'momentum') and hasattr(self, 'momentum_squared'):
      raise ValueError("Channel must have either 'momentum' or 'momentum_suared'")

    if not hasattr(self, 'momentum') and not hasattr(self, 'momentum_squared'):
      self.momentum_squared = 0

    if hasattr(self, 'momentum'):
      self.momentum = tuple(self.momentum)

    if hasattr(self, 'momentum') and self.momentum == (0,0,0):
      del self.momentum
      self.momentum_squared = 0



  @classmethod
  def createFromOperator(cls, operator):
    if operator.isBasicLapH():
      bl_op = operator.getBasicLapH()

      momentum=(bl_op.getXMomentum(), bl_op.getYMomentum(), bl_op.getZMomentum())

      isospin = bl_op.getIsospin().split('_')[0] # Takes care of tetraquarks - Something better?
      if isospin.startswith("iso"):
        isospin = isospin[len("iso"):]
      isospin = Isospin(isospin).to_str()
      strangeness = str(bl_op.getStrangeness())
      flavor = (isospin, strangeness)

      return cls(momentum=momentum, flavor=flavor, irrep=bl_op.getLGIrrep(), irreprow=bl_op.getLGIrrepRow())

    else:
      gi_op = operator.getGenIrrep()

      kw_args = dict()

      kw_args['flavor'] = gi_op.getFlavor()

      if gi_op.getLGIrrep() is not 'NONE':
        kw_args['irrep'] = gi_op.getLGIrrep()

      if gi_op.getLGIrrepRow() > 0:
        kw_args["irreprow"] = gi_op.getLGIrrepRow()

      if gi_op.hasDefiniteMomentum():
        kw_args["momentum"] = (gi_op.getXMomentum(), gi_op.getYMomentum(),
                               gi_op.getZMomentum())
        kw_args["ref_momentum"] = False

      elif gi_op.hasReferenceMomentum():
        kw_args["momentum"] = (gi_op.getXMomentum(), gi_op.getYMomentum(),
                               gi_op.getZMomentum())
        kw_args["ref_momentum"] = True

      elif gi_op.hasMomentumSquared():
        kw_args["momentum_squared"] = gi_op.getMomentumSquared()
        kw_args["ref_momentum"] = False

      return cls(**kw_args)

  @property
  def averaged(self):
    aver_chan = copy.copy(self)
    aver_chan.irreprow = 0
    aver_chan.momentum_squared = self.psq
    if hasattr(self, 'momentum'):
      del aver_chan.momentum
    aver_chan.ref_momentum = False

    return aver_chan

  @property
  def is_averaged(self):
    return self == self.averaged

  @property
  def at_rest(self):
    return self.psq == 0

  @property
  def psq(self):
    if hasattr(self, 'momentum_squared'):
      return self.momentum_squared
    else:
      return self.momentum[0]**2 + self.momentum[1]**2 + self.momentum[2]**2

  @property
  def vev(self):
    return (self.irrep == "A1g" or self.irrep == "A1gp") and (self.flavor == ("0","0") or self.flavor == ("0"))

  def getRotatedOp(self, level=0):
    return self.getGIOperator("ROT", level)

  def getGIOperator(self, obs_name, obs_id=0):
    op_str = "Flavor="
    for flavor_i in self.flavor:
      op_str += f"{flavor_i},"

    op_str = op_str[:-1]

    if hasattr(self, 'momentum_squared'):
      op_str += " PSQ={}".format(self.momentum_squared)

    elif self.ref_momentum:
      op_str += " Pref=({},{},{})".format(self.momentum[0], self.momentum[1],
                                          self.momentum[2])

    else:
      op_str += " P=({},{},{})".format(self.momentum[0], self.momentum[1],
                                       self.momentum[2])

    
    if self.irrep != "NONE":
      op_str += " {}".format(self.irrep)
      if self.irreprow != 0:
        op_str += "_{}".format(self.irreprow)

    op_str += " {} {}".format(obs_name, obs_id)

    return sigmond.GenIrrepOperatorInfo(op_str)

  @property
  def mom_str(self):
    if hasattr(self, 'momentum_squared'):
      return f"PSQ{self.momentum_squared}"
    elif self.ref_momentum:
      return f"Pref{self.momentum[0]}{self.momentum[1]}{self.momentum[2]}"
    else:
      return f"P{self.momentum[0]}{self.momentum[1]}{self.momentum[2]}"

  @property
  def irrep_psq_key(self):
    return f"{self.irrep}_PSQ{self.psq}"

  def __str__(self):
    _str = "Flavor="
    for flavor_i in self.flavor:
      _str += f"{flavor_i},"

    _str = _str[:-1]

    if hasattr(self, "momentum_squared"):
      _str += " PSQ={}".format(self.momentum_squared)
    elif self.ref_momentum:
      _str += " Pref=({},{},{})".format(self.momentum[0], self.momentum[1], self.momentum[2])
    else:
      _str += " P=({},{},{})".format(self.momentum[0], self.momentum[1], self.momentum[2])

    if self.irrep != "NONE":
      _str += f" {self.irrep}"
      if self.irreprow != 0:
        _str += f"_{self.irreprow}"

    return _str
  

  def __repr__(self):
    _str = "F"
    for flavor_i in self.flavor:
      _str += f"{flavor_i}-"

    _str = _str[:-1]

    if hasattr(self, "momentum_squared"):
      _str += "_P{}".format(self.momentum_squared)
    elif self.ref_momentum:
      _str += "_Pr{}{}{}".format(self.momentum[0], self.momentum[1], self.momentum[2])
    else:
      _str += "_P{}{}{}".format(self.momentum[0], self.momentum[1], self.momentum[2])

    if self.irrep != "NONE":
      _str += f"_{self.irrep}"
      if self.irreprow != 0:
        _str += f"_{self.irreprow}"

    return _str.replace('-', 'm')
  
  def __cmp(self):
    mom = self.momentum if hasattr(self, 'momentum') else self.momentum_squared
    #print((self.flavor, self.psq, self.irrep, self.irreprow, mom, self.ref_momentum))
    return (self.flavor, self.psq, self.irrep, self.irreprow, mom, self.ref_momentum)

  def __hash__(self):
    return hash(repr(self))

  def __eq__(self, other):
    return repr(self) == repr(other)

  def __ne__(self, other):
    return not self.__eq__(other)

  def __lt__(self, other):
    if isinstance(other, self.__class__):
      return self.__cmp() < other.__cmp()
    return NotImplemented

  def __le__(self, other):
    if isinstance(other, self.__class__):
      return self.__cmp() <= other.__cmp()
    return NotImplemented

  def __gt__(self, other):
    if isinstance(other, self.__class__):
      return self.__cmp() > other.__cmp()
    return NotImplemented

  def __ge__(self, other):
    if isinstance(other, self.__class__):
      return self.__cmp() >= other.__cmp()
    return NotImplemented
