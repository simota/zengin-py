# -*- coding: utf-8 -*-
from __future__ import division, print_function, absolute_import  # NOQA

from collections import OrderedDict

import six


class BankMeta(type):

    banks = OrderedDict()
    names = {}
    fullnames = {}

    def __setitem__(cls, code, bank):
        cls.banks[code] = bank
        cls.names[bank.name] = bank
        cls.fullnames[bank.fullname] = bank

    def __getitem__(cls, code):
        return cls.banks[code]

    @property
    def all(cls):
        return cls.banks

    def by_name(cls, name):
        bank = cls.names.get(name)
        if bank:
            return bank
        return cls.fullnames.get(name)


class Bank(six.with_metaclass(BankMeta)):

    def __init__(self, code, name, kana, hira, roma, fullname):
        self.code = code
        self.name = name
        self.kana = kana
        self.hira = hira
        self.roma = roma
        self.fullname = fullname
        self.branches = OrderedDict()
        self.named_branches = {}
        self.__class__[code] = self

    def branch_by_name(self, name):
        return self.named_branches.get(name)

    def branch_by_code(self, code):
        return self.branches.get(code)

    def add_branch(self, branch):
        self.branches[branch.code] = branch
        self.named_branches[branch.name] = branch
