# Display average RAM size over the years
st.write('The graph below shows the percentage of RAM size over the years.')
ram = steamdataset.loc[(steamdataset['category'] == 'System RAM')]
ram = ram.groupby(['date', 'name']).agg({'percentage': 'sum'}).reset_index()
ram = ram.pivot(index='date', columns='name', values='percentage')
st.line_chart(ram, use_container_width=True)