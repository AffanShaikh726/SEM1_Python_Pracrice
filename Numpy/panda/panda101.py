# import pandas as pd
import pandas as pd
# import numpy as np
import numpy as np
# simple array
data = np.array(["g", "e", "e", "k", "s"])
ser = pd.Series(data,index=[10, 11, 12, 13, 14])
print(ser)

dict = {"Geeks": 10,
"for": 20,
"geeks": 30
}

# create series from dictionary
ser2 = pd.Series(dict)
print(ser2)