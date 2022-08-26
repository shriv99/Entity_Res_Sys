import pandas as pd
from fuzzywuzzy import process, fuzz
val = input("Enter output result folder path: ")
print(val)
df = pd.read_json(val, lines=True)
df_matches = df[df.match==1]
df_matches = df_matches.rename({'left': 'source_a', 'right': 'source_b'}, axis=1)
df_matches['partial_ratio'] = df_matches.apply(lambda x: fuzz.partial_ratio(x['source_a'], x['source_b']), axis=1 )
df_matches['token_set_ratio'] = df_matches.apply(lambda x: fuzz.token_set_ratio(x['source_a'], x['source_b']), axis=1 )
df_matches['W_ratio'] = df_matches.apply(lambda x: fuzz.WRatio(x['source_a'], x['source_b']), axis=1 )

df_matches.to_excel("Validator_ratio.xlsx")  

