def scale_product_priority(_,input_val):
    output_val = -4.9 * input_val + 9.9 
    return output_val

def normalise(col_name ,input_val):
    limits = params[col_name]
    min = limits["min"]
    max = limits["max"]
    smin = scale["min"]
    smax = scale["max"]
    norm_value = smin + ( input_val - min ) * ( smax - smin ) /( max - min)
    return norm_value

def sprint_val(col_name,input_val):
    if input_val not in valid_sprints:
      return False 
    return True

def is_numeric(value):
    return isinstance(value, (int, float))

def is_int(value):
    return isinstance(value, (int))

def numeric_val(col_name,input_val):
    return is_numeric(input_val)
 
def priority_val(col_name,input_val):
    val = is_numeric(input_val) and  input_val >= params[col_name]["min"] and input_val <= params[col_name]["max"]
    return val
    
params = {
    "requirement effort" : {
       "weight" : 10,
       "min" : 0.1,
       "max" : 200 ,
       "norm_function" : normalise,
       "val_function"  : numeric_val
    },
     "dependency effort" : {
       "weight" : 10,
       "min" : 0.1,
       "max" : 200 ,
       "norm_function" : normalise,
       "val_function"  : numeric_val
    },
    "product priority" : {
       "weight" : 50,
       "min" : 0.1,
       "max" : 200 ,
       "norm_function" : scale_product_priority,
       "val_function"  : priority_val
    },
    "arrival sprint" : {
       "weight" : 30,
       "min" : 1,
       "max" : 4 ,
       "norm_function" : normalise,
       "val_function" : sprint_val
    }
}

scale = {
    "min" : 0.1 ,
    "max" : 5
}

valid_sprints = [ 1,2,3,4]

