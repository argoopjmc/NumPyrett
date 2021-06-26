__version__ = '0.1'
__all__ = ['formatPoly', 'latex_matrix', '__version__']

__author__ = u'Rahul Gupta'
__license__ = 'MIT'
__copyright__ = 'Copyright 2021 Rahul Gupta'


# Source for numpyrett

import numpy as np
import fractions 

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
  return pstr

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
    
    return '\n'.join(rv)
