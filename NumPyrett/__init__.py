__version__ = '1.0'
__all__ = ['formatPoly', 'latex_matrix', '__version__']

__author__ = u'Rahul Gupta'
__license__ = 'MIT'
__copyright__ = 'Copyright 2021 Rahul Gupta'


# Source for numpyrett
# Some code is inspired from StackExchange , namely
# https://stackoverflow.com/questions/3862310/
# https://stackoverflow.com/questions/17129290/
# https://stackoverflow.com/questions/1911281/

import numpy as np
import fractions 
from IPython.display import display, Markdown , Latex

def frac_formatter(coeff , format_mode = False , format_string = '{:0.2f}' , poly_mode = True)->str:
  vals =  str(fractions.Fraction(coeff).limit_denominator()).split('/')
  if(not format_mode):
    if(len(vals)==2):
      if(not format_mode):
        frac = str('\\frac{%d}{%d}' % (abs(int(vals[0])) , abs(int(vals[1]))))
        if(coeff < 0):
          frac = "-" + frac
        return frac
    if(len(vals)==1):
      if(not format_mode):
        if(vals[0] == '1' and poly_mode):
            return " "
        elif(vals[0] == '-1' and poly_mode):
            return "-"
        return vals[0]
    else:
      raise ValueError("Make sure you have typed a valid fraction")
  else:
        return format_string.format(coeff)

def formatPoly(poly , format_mode = False , format_string = '{:0.2f}' ,var_change = False , variable = 'x')->str:
  if (isinstance(poly,np.poly1d)) :
    degree = poly.order
    var = poly.variable if not var_change else variable
    coeff = poly.coef[::-1]
  elif (isinstance(poly,np.polynomial.polynomial.Polynomial)):
    degree = poly.degree()
    var = variable
    coeff = poly.coef[::-1]
    if(coeff[-1] == 0.0):
      coeff = np.resize(coeff, coeff.size - 1)
      degree-=1
  else :
    raise TypeError("You can only pretty print numpy.poly1d or numpy.polynomial.Polynomial")
  pstr =" \\displaystyle "
  
  deg = degree
  while(deg>-1):
        if(coeff[deg]!=0):
            if(deg == degree):
                pstr += frac_formatter(coeff[deg] , format_mode , format_string ) + var + "^{"+ str(deg) + "}"
            else:
                prefix = " " if ("-" in str(coeff[deg])) else " + "
                if(deg>1):
                    pstr += prefix + frac_formatter(coeff[deg] , format_mode , format_string) + var + "^"+ str(deg)
                elif(deg == 1):
                    pstr += prefix +  frac_formatter(coeff[deg] , format_mode , format_string) + var + ""
                elif(deg == 0):
                    pstr += prefix + frac_formatter(coeff[deg] , format_mode , format_string)
        deg = deg - 1
  # pstr+='$'
  display(Latex(pstr))

def latex_matrix(array , mat_type = 'bmatrix' , format_mode = False , format_string = '{:0.2f}' ):
    if isinstance(array,np.matrix):
        array = np.squeeze(np.asarray(array))
    if len(array.shape) > 2:
        raise ValueError('bmatrix can at most display two dimensions')

    temp_array = np.empty(array.shape)
    
    if len(array.shape) == 1:
      temp_array = np.array(list(map(lambda x: frac_formatter(x,format_mode,format_string,False) , array)))
    if len(array.shape) == 2:
      for row in array:
        row = np.array(list(map(lambda x: frac_formatter(x,format_mode,format_string,False) , row)))
        temp_array = np.vstack([temp_array,row])
      temp_array = temp_array[array.shape[0]:]

    lines = str(temp_array).replace('[', '').replace(']', '').replace('\'', '').replace('\\\\', '\\').splitlines()
    rv = [r'\begin{' + mat_type + '}']
    rv += ['  ' + ' & '.join(l.split()) + r'\\' for l in lines]
    rv +=  [r'\end{' + mat_type + '}']
    
    display(Latex('\n'.join(rv)))

def pretty_list(lst,index_colour_pair_dict= {0:'red'}):
  array_str = ""
  for i in range(len(lst)):
    if i in index_colour_pair_dict.keys():
      array_str+=fr"\fcolorbox{{{index_colour_pair_dict.get(i)}}}{{{index_colour_pair_dict.get(i)}}}{{{lst[i]}}}"
    else:
      array_str+=fr"\fbox{{{lst[i]}}}"
  display(Latex (array_str))

def get_all_subclasses(obj):
    all_subclasses = []
    for subclass in obj.__subclasses__():
        all_subclasses.append(subclass.__name__)
        all_subclasses.extend(get_all_subclasses(subclass))
    return set(all_subclasses)

def get_all_superclasses(obj):
    all_superclasses = []
    for superclass in obj.__bases__:
        all_superclasses.append(superclass.__name__)
        all_superclasses.extend(get_all_superclasses(superclass))
    
    return set(all_superclasses)

def get_all_fields(obj):
    return set(obj.__dict__.keys())

def get_all_methods(obj):
  return set([func for func in dir(obj.__class__) if callable(getattr(obj.__class__, func)) and not func.startswith("__")])

def class_info(obj):
  display(Markdown(fr'# Class {obj.__class__.__name__}'))
  display(Markdown(fr'## Super Classes : { get_all_superclasses(obj.__class__) }'))
  display(Markdown(fr'## Sub Classes   : { get_all_subclasses(obj.__class__) }'))
  display(Markdown(fr'## Fields        : { get_all_fields(obj) }'))
  display(Markdown(fr'## Methods       : { get_all_methods(obj) }'))
 