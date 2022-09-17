import streamlit as st

def app(df):
	st.header('Early Diabetes Prediction Web App')
	st.markdown("<p style='color:red;font-size:20px'> Diabetes is a chronic (long-lasting) health condition that affects how your body turns food into energy.There isn’t a cure yet for diabetes, but losing weight, eating healthy food, and being active can really help in reducing the impact of diabetes.This Web app will help you to predict whether a person has diabetes or is prone to get diabetes in future by analysing the values of several features using the Decision Tree Classifier. </p>" , unsafe_allow_html = True)

	st.subheader('View Data')
	with st.beta_expander('View Data'):
		st.dataframe(df)

	st.title('Columns Description')
	c1,c2,c3 = st.beta_columns(3)

	with c1:
		if st.checkbox('Show all column names'):
			st.table(df.columns)
	with c2:
		if st.checkbox('View column data-type'):
			st.table(df.astype(str))
	with c3:
		if st.checkbox('View column data'):
			column = st.selectbox('Select Column' , tuple(df.columns))
			st.write(df[column])

	if st.checkbox('Show summary'):
		st.table(df.describe())