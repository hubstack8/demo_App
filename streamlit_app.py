import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("🔍 Dummy EDA Dashboard for Paper Review")

# Create dummy plots
def create_line_plot():
    x = np.arange(10)
    y = np.random.rand(10)
    fig, ax = plt.subplots()
    ax.plot(x, y, marker='o')
    ax.set_title("Line Plot: Random Trend")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    return fig

def create_bar_plot():
    categories = ['A', 'B', 'C', 'D']
    values = np.random.randint(1, 20, size=4)
    fig, ax = plt.subplots()
    ax.bar(categories, values, color='skyblue')
    ax.set_title("Bar Plot: Category Counts")
    return fig

def create_histogram():
    data = np.random.randn(1000)
    fig, ax = plt.subplots()
    ax.hist(data, bins=30, color='green', alpha=0.7)
    ax.set_title("Histogram: Normal Distribution")
    return fig

def create_scatter_plot():
    x = np.random.rand(50)
    y = np.random.rand(50)
    colors = np.random.rand(50)
    sizes = 100 * np.random.rand(50)
    fig, ax = plt.subplots()
    scatter = ax.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='viridis')
    ax.set_title("Scatter Plot1: Random Points")
    fig.colorbar(scatter, ax=ax, label='Color Scale')
    return fig

def create_pie_chart():
    labels = ['Python', 'C++', 'Ruby', 'Java']
    sizes = [215, 130, 245, 210]
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.set_title("Pie Chart: Language Usage")
    ax.axis('equal')
    return fig

# Put plots in tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "Line Plot", "Bar Plot", "Histogram", "Scatter Plot", "Pie Chart"
])

with tab1:
    st.pyplot(create_line_plot())
    st.caption("Figure 1: Random line plot showing a sample trend.")

with tab2:
    st.pyplot(create_bar_plot())
    st.caption("Figure 2: Bar chart displaying category counts.")

with tab3:
    st.pyplot(create_histogram())
    st.caption("Figure 3: Histogram of a normal distribution.")

with tab4:
    st.pyplot(create_scatter_plot())
    st.caption("Figure 4: Scatter plot with random points and color scale.")

with tab5:
    st.pyplot(create_pie_chart())
    st.caption("Figure 5: Pie chart of language usage proportions.")
