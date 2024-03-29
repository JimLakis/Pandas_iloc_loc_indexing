# Python v3.6


import pandas as pd


def load_CSV():
    df = pd.read_csv('uk-500.csv', delimiter=',')
    return df


def practice_retreiving_values(df):
    def retrieve_rows(df):
        ''' Returns all rows where 'county' equals Derbyshire, display all columns.
            Output type is a Series. '''
        return df.loc[df["county"] == "Derbyshire"]

    def retrieve_rows_and_specific_column(df):
        ''' Returns all rows where 'county' equals Derbyshire, display only the columns 'phone1'.
            Output type is a DataFrame. '''
        return df.loc[df["county"] == "Derbyshire", ["phone1"]]
        
    #results = retrieve_rows(df)
    results = retrieve_rows_and_specific_column(df)
    print(results)
	
	
def assign_values_w_loc(df):
    ''' Assign all rows' "phone1" values to "00000-000000" where "county" equals "Derbyshire".
        This is done inplace, ie on the same dataframe '''
    df.loc[df["county"] == "Derbyshire", ["phone1"]] = "00000-000000"


def main():
    df = load_CSV()
    df.set_index("last_name", inplace=True)

	#practice_retreiving_values(df)

	assign_values_w_loc(df)
    print(df.loc[df["county"] == "Derbyshire", ["phone1"]])


if __name__ == '__main__':
    main()