# %% [markdown]
# #  Inventory Management Dashboard and Analysis

# %% [markdown]
# ## <mark>1. Read & describe the data 

# %%
# PeakFit_analysis csv data reading
import pandas as pd
import numpy as np

import altair as alt
import panel as pn
import plotly.graph_objects as go
import plotly.express as px
pn.extension('plotly')
ACCENT = "teal"


# %%
df = pd.read_excel(r'D:\K_REPO\Depi_freelanceYard\PeakFit Essentials.xlsx',sheet_name='Sheet1')
df.sort_values(by="Date").head(5)

# %% [markdown]
# ## <mark>2. Clean the data 

# %%
#drop unusfull columns
df = df.drop(columns=['Expired Items','Returned Items','Items Out for Sales','Items Out for Quality Control','Items Out for Events'])

# %%
df["Date"] = pd.to_datetime(df["Date"], format="%Y-%m-%d")

# %%
#replace expected & actual with stocked quantity
#make column for Inventory Discrepancy
df['Inventory Discrepancy'] =  df['Actual Quantity'] - df['Expected Quantity']
df = df.drop(columns=['Expected Quantity',	'Actual Quantity'  ])
print(df['Inventory Discrepancy'].sum())  #total Inventory Discrepancy in 10 monthes [ -N : missing , +N more than expeted  ] 
df.head()

# %%
df['Month'] = df['Date'].dt.month_name()


# %%
print(df['Inventory Discrepancy'].sum())

# %% [markdown]
# ### the new data discription

# %%
df.info()

# %%
df.describe(include='all')

# %% [markdown]
# Date started 2024-01-01  ended 2024-09-30 with 2000 record .
# 
# time 3 shifts per day (morning, afternoon, evening).
# 
# item ID are only 6 items (Dumbbells, Yoga Mat, Resistance Bands, Protein Powder, Foam Roller, Kettlebells).
# 
# category are only 3 items , but 4 in category sheet (Strength Training Equipment, fitness accessories, strength training equipment). there is an issue (miss leading inputs)
# 
# responsible staff are only 6 (['Robert Tabone', 'Simon Fenech', 'Jean-Pierre Ellul','Andrew Cauchi', 'Aaron Vella', 'Franklin Attard']).
# 
# and no nulls in the data
# 
# 

# %%
# fixing category
# assinge ITM001 , ITM003 , ITM006 to ctg001  as they all strength training Items
df.loc[df['Item ID'].isin(['ITM001', 'ITM003', 'ITM006']), 'Category'] = 'CTG001'

# assinge ITM004 as CTG004 ( protein poweder is supplements )
df.loc[df["Item ID"].isin(["ITM004"]), "Category"]= "CTG003"

#assinge ITM005 as CTG005 (foam rollers are recovery tools)
df.loc[df["Item ID"].isin(["ITM005"]), "Category"]="CTG004"

df['Category'].unique()


# %% [markdown]
# ## <mark>3. Data proccessing

# %% [markdown]
# #### calender heatmap (Heat_fig) ####

# %%
# Convert DateTime to datetime format
df['DateTime'] = pd.to_datetime(df['Date'])

# Extract Month and Day
df['Month'] = df['DateTime'].dt.strftime('%B')  # Month name
df['Day'] = df['DateTime'].dt.day  # Day of month

# Aggregate data by Day and Month (sum of Inventory Discrepancy)
df_agg = df.groupby(['Day', 'Month'])['Inventory Discrepancy'].sum().reset_index()

# Create pivot table for heatmap
heatmap_data = df_agg.pivot(index='Day', columns='Month', values='Inventory Discrepancy')

# Fill NaN values with 0 (days with no Inventory Discrepancy)
heatmap_data = heatmap_data.fillna(0)

# Define month order for proper sorting
month_order = ["January", "February", "March", "April", "May", "June", 
               "July", "August", "September", "October"]

# Filter to only include months that are in our data
available_months = [month for month in month_order if month in heatmap_data.columns]
heatmap_data = heatmap_data.reindex(columns=available_months)
df_agg.head()

# %%

# Create the heatmap
Heat_fig = px.imshow(
    heatmap_data.values,
    labels=dict(x="Month", y="Day", color="Inventory Discrepancy"),
    x=heatmap_data.columns,
    y=heatmap_data.index,
    color_continuous_scale="RdBu",  # Changed to Reds as Inventory Discrepancy are positive now
    text_auto=True  # Display values in the cells
)

Heat_fig.update_layout(
    title="Inventory Discrepancy/day Heatmap",
    xaxis_title="Month",
    yaxis_title="Day of Month",

    yaxis=dict(
        range=[1, 31],  # Explicitly reverse the order (assuming max day is 31)
        autorange=False  # Disable automatic range adjustment
        ),  # Keep day labels in correct order
   
    width=700,  # Set width
    height=600,   # Set height
    plot_bgcolor="black",  # Set plot background to black
    paper_bgcolor="white",  # Set entire figure background to black
    font=dict(color="black")  # Set text color to white for contrast
    
)

# To display the figure

Heat_fig

# %% [markdown]
# #made a calnder as heatmap, and found :
# 
# at (25/07) 31 unexpected item found 
# 
# at (30/05) & 03/08 highest missing record at -23 item 

# %% [markdown]
# #### by weekday (Bar_fig)

# %%
# Extract weekday name
df["Weekday"] = df["Date"].dt.day_name()
# Group by weekday and sum Inventory Discrepancy
df_grouped = df.groupby("Weekday")["Inventory Discrepancy"].sum().reset_index()
# Define weekday order
weekday_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# Create a category type with our custom order
df_grouped["Weekday"] = pd.Categorical(df_grouped["Weekday"], categories=weekday_order, ordered=True)

# Sort by our ordered category
df_grouped = df_grouped.sort_values("Weekday")

# # Create color sequence to match your original
# colors = ["skyblue", "orange", "green", "red", "purple", "pink", "brown"]

df.head()

# %%
# Create the bar chart
Bar_fig = px.bar(
    df_grouped,
    x="Weekday",
    y="Inventory Discrepancy",
    title="Inventory Discrepancy by Day of the Week",
    color="Inventory Discrepancy",  # Color by value
    color_continuous_scale=['red', 'blue'],  # Red for negative, blue for positive
    labels={"Weekday": "Day of the Week", "Inventory Discrepancy": "Total Inventory Discrepancy"}
)

# Update layout for dark background
Bar_fig.update_layout(
    plot_bgcolor="black",  # Set plot background to black
    paper_bgcolor="black",  # Set entire figure background to black
    font=dict(color="white")  # Set text color to white for contrast
)

# Add grid lines
Bar_fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='rgba(255,255,255,0.2)')

component0 = pn.panel(Bar_fig)
# Display the figure
Bar_fig


# %% [markdown]
# allover the week tuesdays were for losing items . about 94 item were missed   

# %% [markdown]
# ### staff sum of recorded stocks  allover the year (Bar2_fig)

# %%
#Inventory Discrepancy per staff
df_miss_perstaff=df.groupby("Responsible Staff").agg({
    'Inventory Discrepancy': 'sum'
})
df_miss_perstaff.head(10)

# %% [markdown]
# franklin & jean were responsible for most missing recordes  ( 39 , 11)

# %% [markdown]
# ### shifts and responsible staff (Line_fig)

# %%
#staff per shift
df_staff_shifts = df.groupby(["Responsible Staff", "Time"]).size().unstack(fill_value=0)
df_staff_shifts["Total Shifts"] = df_staff_shifts.sum(axis=1)
df_staff_shifts.head(10)

# %%

# Data
staff = ["Aaron Vella", "Andrew Cauchi", "Franklin Attard", "Jean-Pierre Ellul", "Robert Tabone", "Simon Fenech"]
shifts = ["Morning", "Afternoon", "Evening"]
morning = [104, 96, 106, 122, 123, 128]
afternoon = [103, 110, 115, 106, 106, 104]
evening = [107, 106, 98, 140, 124, 102]

# Define custom colors for each staff member
colors = ['blue', 'red', 'green', 'purple', 'orange', 'brown']

# Create figure with specified name
Line_fig = go.Figure()

# Add traces for each staff member with specific colors
for i, staff_name in enumerate(staff):
    y_values = [morning[i], afternoon[i], evening[i]]
    Line_fig.add_trace(go.Scatter(
        x=shifts,
        y=y_values,
        mode='lines+markers',
        name=staff_name,
        line=dict(color=colors[i], width=2),
        marker=dict(color=colors[i], size=8),
        hovertemplate='<b>%{x} Shift</b><br>' + 
                     f'{staff_name}: ' + '%{y}<extra></extra>'
    ))

# Update layout
Line_fig.update_layout(
    title="Shift Distribution Across Staff Members",
    xaxis_title="Shifts",
    yaxis_title="Shift Distribution",
    legend_title="Staff Members",
    height=600,
    width=800,
    hovermode="closest"
)

# Add grid lines for better readability
Line_fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='rgba(0,0,0,0.1)')
Line_fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='rgba(0,0,0,0.1)')

# Show the figure
Line_fig

# %% [markdown]
# ### final stocks of Items

# %%
df_stocks = df.groupby(["Item ID", "Category"])["Inventory Discrepancy"].agg(sum)
pd.DataFrame(df_stocks).head(10)

# %% [markdown]
# ITM002 & ITM005 are the missed itmes : (Yoga Mat: 71 missing , foam rollers: 42 missing) 

# %% [markdown]
# ## the interactive bar chart (fig)

# %%
#make a df to customize
activ_df = pd.DataFrame(df[["Time", "Month","Responsible Staff","Category","Inventory Discrepancy"]])
activ_df.head()

# %%
# Create a vertical radio button group
list_dropdown = pn.widgets.RadioButtonGroup(
    name="Select Data on X axis",
    options=["Date", "Month", "Time", "Responsible Staff", "Category", "Item ID" , "Weekday"],
    description="select data type to calculate stock for!",
    button_style='outline'
)

# Wrap in a Panel component (optional, but can help with layout)
component1 = pn.panel(list_dropdown)
list_dropdown

# %%

@pn.depends(list_dropdown)
def inter_bar(list_dropdown):
    # Aggregate data for plotting
    grouped_df = df.groupby(list_dropdown)['Inventory Discrepancy'].sum().reset_index()
    
    # Ensure 'Month' column is ordered correctly if the dropdown is "Month"
    if list_dropdown == "Month":
        grouped_df["Month"] = pd.Categorical(grouped_df["Month"], categories=month_order, ordered=True)
        grouped_df = grouped_df.sort_values("Month")

    # Set title dynamically
    tit = "Missing/overstock by item ID" if list_dropdown == "item ID" else f'Inventory Discrepancy by {list_dropdown}'

    # Create the figure using Plotly Express
    fig = px.bar(
        grouped_df,
        x=list_dropdown,
        y="Inventory Discrepancy",
        title=tit,
        color="Inventory Discrepancy",  # Color by category
        color_continuous_scale=['red', ACCENT],  # Adjust color scale
    )
        # Improve layout
    fig.update_layout(
        xaxis_title=list_dropdown,
        yaxis_title="Total Inventory Discrepancy",
        plot_bgcolor="#f8f8f8",  
        paper_bgcolor="#f8f8f8",  
        font=dict(color="black"),  
        xaxis=dict(gridcolor='lightgray', showgrid=True),
        yaxis=dict(gridcolor='black'),
        width=1200,  
        height=500,
    )
    
    return fig

component2 = pn.panel(inter_bar)  # Assign to Panel

inter_bar("Month")  # Show ordered months

    


# %% [markdown]
# ## creating KPIs cards 

# %% [markdown]
# total actual stock= 94489
# 
# total expected stock= 94447
# 
# total overstock= 42 (.044% of the stock)
# 
# ITM002(Yoga Mat) lost 71 pieces , ITM005(Foam Roller) lost 42 piece,  totlal= 113
# 
# the over stock items (ITM001: 16 , ITM003: 35 , ITM004: 35 , ITM006: 69), total= 155

# %%
ACCENT = "teal"

styles = {
    "box-shadow": "rgba(50, 50, 93, 0.25) 0px 6px 12px -2px, rgba(0, 0, 0, 0.3) 0px 3px 7px -3px",
    "border-radius": "10px",
    "padding": "10px",
    "background": "#DCEFF0",
    'box-shadow': "3px 3px 6px rgba(0,0,0,0.3)",
    "width": "385px",
    "height": "220px" 
    }               # a dict to use later in the cards 


# %%
# KPIs cards
cards= pn.FlexBox(



    #'Highest miss/day
    pn.indicators.Number(name='The worst-performing day <br> (03.Aug & 30.May)📉',
    value=23, 
    format='<span style="font-size:1.5em;">{value}</span>'
       '<span style="font-size:0.7em;"> items</span>',
    colors=[(1, 'black')],
    styles=styles,
    ),

    pn.indicators.Number(
    name='Franklin Attard <br> the biggest Loser',
    value=39,
    # Embed HTML to style the units separately:
    format='<span style="font-size:1.5em;">{value}</span>'
           '<span style="font-size:0.7em;"> items</span>',
    colors=[(0, ACCENT)]
    ,styles=styles
    ),

    pn.indicators.Number(
    name='Morning shift had the <br> hieghest missing rate',
    value=84,
    # Embed HTML to style the units separately:
    format='<span style="font-size:1.5em;">{value}</span>'
           '<span style="font-size:0.7em;"> items</span>',
    colors=[(0, ACCENT)]
    ,styles=styles
    )
)



# %%
cards

# %% [markdown]
# ### making cards of stock discrepancy

# %%


# Data for missing and overstocked items
missing_items = {
    "Yoga Mat": 71,
    "Foam Roller": 42
}
overstock_items = {
    "Dumbbells": 16,
    "Resistance Band": 35,
    "Jump Rope": 35,
    "Kettlebell": 69
}

# Convert to DataFrame
df_missing = pd.DataFrame(missing_items.items(), columns=["Item", "Quantity Lost"])
df_overstock = pd.DataFrame(overstock_items.items(), columns=["Item", "Quantity Overstocked"])


# %%

# Create bar plots
fig_missing = px.bar(
    df_missing, 
    x="Item", 
    y="Quantity Lost", 
    title="Missing Items(max:71, sum:113)", 
    color="Quantity Lost",
    color_continuous_scale=[(0, "lightcoral"), (0.5, "red"), (1, "darkred")]

)



fig_overstock = px.bar(
    df_overstock, 
    x="Item", 
    y="Quantity Overstocked", 
    title="Overstocked Items(max:69, sum:155)", 
    color="Quantity Overstocked",
    color_continuous_scale="blues"
)

# Improve layout
fig_missing.update_layout(paper_bgcolor="#DCEFF0", plot_bgcolor="#DCEFF0", width=295, height=295, coloraxis_showscale=False,title_font=dict(size=16))
fig_overstock.update_layout(paper_bgcolor="#DCEFF0", plot_bgcolor="#DCEFF0", width=295, height=295,coloraxis_showscale=False,title_font=dict(size=14) )

component3=pn.panel(fig_missing)
component4=pn.panel(fig_overstock)


# %%

# Convert to DataFrame
df_missing = pd.DataFrame(missing_items.items(), columns=["Item", "Quantity Lost"])
df_overstock = pd.DataFrame(overstock_items.items(), columns=["Item", "Quantity Overstocked"])

# Create bar plots
fig_missing = px.bar(
    df_missing, 
    x="Item", 
    y="Quantity Lost", 
    title="Missing Items(max:71, sum:113)", 
    color="Quantity Lost",
    color_continuous_scale=[(0, "lightcoral"), (0.5, "red"), (1, "darkred")]
)


missing_items_indicator = pn.indicators.Number(
    name="Missing Items",  # Title
    value=113,  # Number displayed
    format="{:.0f}",  # No decimal places
    colors=[(50, "red")],  # Customize color if needed
    font_size="20pt"  # Adjust font size
)


fig_overstock = px.bar(
    df_overstock, 
    x="Item", 
    y="Quantity Overstocked", 
    title="Overstocked Items(max:69, sum:155)", 
    color="Quantity Overstocked",
    color_continuous_scale="blues"
)

# Improve layout
fig_missing.update_layout(
    paper_bgcolor="#DCEFF0",
    plot_bgcolor="#DCEFF0",
    width=600,
    height=295,
    coloraxis_showscale=False,
    title_font=dict(size=28, color="#8B0000")  # Set title color to red
)

fig_overstock.update_layout(
    paper_bgcolor="#DCEFF0",
    plot_bgcolor="#DCEFF0",
    width=600,
    height=295,
    coloraxis_showscale=False,
    title_font=dict(size=28, color="teal")  # Set title color to blue
)


component3=pn.panel(fig_missing)
component4=pn.panel(fig_overstock)
comp5=pn.panel(missing_items_indicator)


# %% [markdown]
# ## Dashboard layout

# %%
styles2 = {
    "box-shadow": "rgba(50, 50, 93, 0.25) 0px 6px 12px -2px, rgba(0, 0, 0, 0.3) 0px 3px 7px -3px",
    "border-radius": "10px",
    "padding": "10px",
    "background": "#DADADA",
    'box-shadow': "3px 3px 6px rgba(0,0,0,0.3)",
    "width": "280px",
    "height": "80px" 
    }  
sidebar_card1 = pn.indicators.Number(
    name=("Total records: 2000"),
    styles=styles2
    
)

sidebar_card2 = pn.indicators.Number(
    name=("Start date: 01-01-2024  To 30-09-2024"),
    styles=styles2
)

insight1 = pn.indicators.Number(
    name="More managment on Morinig shift is essential ",
    styles={"background": "#6AB187", "border-radius": "10px", "padding": "10px", "width": "300" , "height":"120px"}
)

insight2 = pn.indicators.Number(
    name="light items must be moved in more watched ereas ",
    styles={"background": "#6AB187", "border-radius": "10px", "padding": "10px", "width": "300" , "height":"120px"}
)

insight3 = pn.indicators.Number(
    name="need better rocording system to overcome the overstocking issue",
    styles={"background": "#6AB187", "border-radius": "10px", "padding": "10px", "width": "300" , "height":"120px"}
)


# %%
import panel as pn

# Create the template
template = pn.template.EditableTemplate(
    title="PeakFit Inventory Analysis Interactive Dashboard",
    theme="default",
    header_background="#1C4E80",  # Header background color
    
    sidebar=[
        pn.pane.Markdown("Inventory Infos & Insights"),  # Sidebar title
        pn.pane.Image(
            "D:\K_REPO\Depi_freelanceYard\images.png",
            width=290,  # Adjust width as needed
            align="center"
        ),
        sidebar_card1,
        sidebar_card2,
        insight1,
        insight2,
        insight3
    ],
    sidebar_width=300,  # Adjust sidebar width
)



# Add main content
template.main.append(
    pn.Column(
        # Row 1: Charts
        pn.Row(component3, component4, sizing_mode="stretch_width"),  

        # Row 2: KPI Cards
        pn.Row(cards, sizing_mode="stretch_width"),  

        # Row 3: Stacked Components
        pn.Column(
            pn.Row(component2, sizing_mode="stretch_width"),  
            pn.Row(pn.Spacer(width=200), component1, sizing_mode="stretch_width"),  
        ),
    )
)

template.servable()



