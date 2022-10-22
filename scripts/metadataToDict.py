
"""
Converts metadata from a file to a dictionary.
"""

import pandas as pd

def metadataHelper(filetype):
	"""
	Helper function to convert metadata to a dictionary.
	input: datatype (string) | Valid options: 'Policies', 'Claims'
	output: metadata (dictionary)
	"""
	# Non Nominal Number (Numerical) Columns
	# In Claims Dataset
	listNonNominalNumberClaimsColumns = ["policyCount","numberOfFloorsInTheInsuredBuilding",
	"amountPaidOnBuildingClaim","amountPaidOnContentsClaim",
	"amountPaidOnIncreasedCostOfComplianceClaim",
	"totalBuildingInsuranceCoverage","totalContentsInsuranceCoverage"]

	# In Policies Dataset
	listNonNominalNumberPoliciesColumns = ["deductibleAmountInBuildingCoverage","deductibleAmountInContentsCoverage",
	"latitude","longitude","numberOfFloorsInInsuredBuilding","policyCost",
	"policyCount","totalBuildingInsuranceCoverage","totalContentsInsuranceCoverage",
	"totalInsurancePremiumOfThePolicy"]                       

	# Read in metadata file and Add Python Data Type Column
	if filetype == "Claims":
		Metadata = pd.read_csv(r"data\\NfipFimaClaimsMetaData.txt", sep="\t")
		Metadata["PythonDataType"] = Metadata["Type"].map({"string": "str","boolean":"str","number": "str", "date": "str"})
		Metadata = Metadata.reset_index(drop=True)
		for index,row in Metadata.iterrows():
			# Convert only financial columns to float 
			if row["Name"] in listNonNominalNumberClaimsColumns:
				Metadata.at[index, "PythonDataType"] = "float"

	elif filetype == "Policies":
		Metadata = pd.read_csv(r"data\\NfipFimaPoliciesMetaData.txt", sep="\t")
		Metadata["PythonDataType"] = Metadata["Type"].map({"string": "str","boolean":"str","number": "str", "date": "str"})
		Metadata = Metadata.reset_index(drop=True)
		for index,row in Metadata.iterrows():
			print(type(index), type(row))
			# Convert only financial columns to float 
			if row["Name"] in listNonNominalNumberClaimsColumns:
				Metadata.at[index, "PythonDataType"] = "float"

	# Convert to dictionary
	metadata_dict = Metadata.set_index('Name').to_dict()['PythonDataType']

	# Returns Dictionary
	return metadata_dict