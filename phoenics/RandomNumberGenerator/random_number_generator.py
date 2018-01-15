#!/usr/bin/env python 

__author__ = 'Florian Hase'

#========================================================================

import numpy as np 

#========================================================================

class RandomNumberGenerator(object):

	def __init__(self):
		pass


	def _normal_float(self, var_dict, size):
		return np.random.normal(loc = var_dict['loc'], scale = var_dict['scale'], size = size)

	def _uniform_float(self, var_dict, size):
		return np.random.uniform(low = var_dict['low'], high = var_dict['high'], size = size)


	def generate(self, var_dict, size, kind = 'uniform'):
		if kind == 'uniform' and var_dict['type'] == 'float':
			return self._uniform_float(var_dict, size)
		elif kind == 'normal' and var_dict['type'] == 'float':
			return self._uniform_float(var_dict, size)
		else:
			raise NotImplementedError()