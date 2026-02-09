import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="Teens & Social Media", layout="wide")
st.title("How Often Teens Say They Use Each Platform")

categories = ['Facebook', 'Instagram', 'Snapchat', 'TikTok', 'YouTube']
data = {
    "Almost constantly": [2, 10, 15, 16, 19],
    "Several times a day": [8, 27, 29, 32, 41],
    "About once a day": [8, 12, 7, 9, 17],
    "Less often": [14, 12, 8, 9, 18],
    "Don't use": [67, 38, 41, 33, 5]
}
colors = ['#0080ff', '#00bfff', '#87cefa', '#add8e6', '#d3d3d3']

fig = go.Figure()
for i, (label, values) in enumerate(data.items()):
    fig.add_trace(go.Bar(
        y=categories, x=values, name=label, orientation='h',
        marker=dict(color=colors[i], line=dict(color='white', width=1)),
        text=[f"{v}%" if v > 5 else "" for v in values],
        textposition='inside'
    ))

fig.update_layout(barmode='stack', yaxis=dict(autorange="reversed"), height=600)
st.plotly_chart(fig, use_container_width=True)
