import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Film Production Data Hub Dashboard",
    page_icon="🎬",
    layout="wide"
)

# -----------------------------
# CSS Styling
# -----------------------------
st.markdown(
    """
    <style>
    .main {
        background-color: #f8fafc;
    }

    .title-box {
        background: linear-gradient(135deg, #0f172a, #1e3a8a);
        padding: 35px;
        border-radius: 22px;
        color: white;
        margin-bottom: 25px;
    }

    .title-box h1 {
        font-size: 42px;
        margin-bottom: 10px;
    }

    .title-box p {
        font-size: 18px;
        color: #dbeafe;
    }

    .section-box {
        background-color: white;
        padding: 25px;
        border-radius: 18px;
        box-shadow: 0 10px 25px rgba(15, 23, 42, 0.08);
        margin-bottom: 25px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# Header
# -----------------------------
st.markdown(
    """
    <div class="title-box">
        <h1>🎬 Film Production Data Hub Dashboard</h1>
        <p>
        Analyze movie production data including title, director, year, genre, budget, revenue, profit, and ROI.
        This dashboard connects film production with data visualization.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# 50 Movie Sample Data
# -----------------------------
default_movies = [
    {"Title": "Titanic", "Director": "James Cameron", "Year": 1997, "Genre": "Romance", "Budget": 200_000_000, "Revenue": 2_264_000_000},
    {"Title": "Avatar", "Director": "James Cameron", "Year": 2009, "Genre": "Sci-Fi", "Budget": 237_000_000, "Revenue": 2_923_000_000},
    {"Title": "The Godfather", "Director": "Francis Ford Coppola", "Year": 1972, "Genre": "Crime", "Budget": 6_000_000, "Revenue": 250_000_000},
    {"Title": "Parasite", "Director": "Bong Joon-ho", "Year": 2019, "Genre": "Thriller", "Budget": 11_400_000, "Revenue": 263_000_000},
    {"Title": "The Dark Knight", "Director": "Christopher Nolan", "Year": 2008, "Genre": "Action", "Budget": 185_000_000, "Revenue": 1_006_000_000},

    {"Title": "Jaws", "Director": "Steven Spielberg", "Year": 1975, "Genre": "Thriller", "Budget": 9_000_000, "Revenue": 476_000_000},
    {"Title": "Star Wars", "Director": "George Lucas", "Year": 1977, "Genre": "Sci-Fi", "Budget": 11_000_000, "Revenue": 775_000_000},
    {"Title": "E.T. the Extra-Terrestrial", "Director": "Steven Spielberg", "Year": 1982, "Genre": "Sci-Fi", "Budget": 10_500_000, "Revenue": 792_000_000},
    {"Title": "Back to the Future", "Director": "Robert Zemeckis", "Year": 1985, "Genre": "Adventure", "Budget": 19_000_000, "Revenue": 388_000_000},
    {"Title": "Jurassic Park", "Director": "Steven Spielberg", "Year": 1993, "Genre": "Adventure", "Budget": 63_000_000, "Revenue": 1_109_000_000},

    {"Title": "Forrest Gump", "Director": "Robert Zemeckis", "Year": 1994, "Genre": "Drama", "Budget": 55_000_000, "Revenue": 678_000_000},
    {"Title": "The Lion King", "Director": "Roger Allers and Rob Minkoff", "Year": 1994, "Genre": "Animation", "Budget": 45_000_000, "Revenue": 968_000_000},
    {"Title": "Pulp Fiction", "Director": "Quentin Tarantino", "Year": 1994, "Genre": "Crime", "Budget": 8_000_000, "Revenue": 214_000_000},
    {"Title": "Toy Story", "Director": "John Lasseter", "Year": 1995, "Genre": "Animation", "Budget": 30_000_000, "Revenue": 394_000_000},
    {"Title": "Independence Day", "Director": "Roland Emmerich", "Year": 1996, "Genre": "Sci-Fi", "Budget": 75_000_000, "Revenue": 817_000_000},

    {"Title": "The Matrix", "Director": "The Wachowskis", "Year": 1999, "Genre": "Sci-Fi", "Budget": 63_000_000, "Revenue": 467_000_000},
    {"Title": "Gladiator", "Director": "Ridley Scott", "Year": 2000, "Genre": "Action", "Budget": 103_000_000, "Revenue": 465_000_000},
    {"Title": "Harry Potter and the Sorcerer's Stone", "Director": "Chris Columbus", "Year": 2001, "Genre": "Fantasy", "Budget": 125_000_000, "Revenue": 1_024_000_000},
    {"Title": "The Lord of the Rings: The Fellowship of the Ring", "Director": "Peter Jackson", "Year": 2001, "Genre": "Fantasy", "Budget": 93_000_000, "Revenue": 898_000_000},
    {"Title": "Spider-Man", "Director": "Sam Raimi", "Year": 2002, "Genre": "Action", "Budget": 139_000_000, "Revenue": 825_000_000},

    {"Title": "Finding Nemo", "Director": "Andrew Stanton", "Year": 2003, "Genre": "Animation", "Budget": 94_000_000, "Revenue": 940_000_000},
    {"Title": "The Lord of the Rings: The Return of the King", "Director": "Peter Jackson", "Year": 2003, "Genre": "Fantasy", "Budget": 94_000_000, "Revenue": 1_147_000_000},
    {"Title": "Shrek 2", "Director": "Andrew Adamson", "Year": 2004, "Genre": "Animation", "Budget": 150_000_000, "Revenue": 935_000_000},
    {"Title": "Batman Begins", "Director": "Christopher Nolan", "Year": 2005, "Genre": "Action", "Budget": 150_000_000, "Revenue": 373_000_000},
    {"Title": "Pirates of the Caribbean: Dead Man's Chest", "Director": "Gore Verbinski", "Year": 2006, "Genre": "Adventure", "Budget": 225_000_000, "Revenue": 1_066_000_000},

    {"Title": "Iron Man", "Director": "Jon Favreau", "Year": 2008, "Genre": "Action", "Budget": 140_000_000, "Revenue": 585_000_000},
    {"Title": "Slumdog Millionaire", "Director": "Danny Boyle", "Year": 2008, "Genre": "Drama", "Budget": 15_000_000, "Revenue": 378_000_000},
    {"Title": "Up", "Director": "Pete Docter", "Year": 2009, "Genre": "Animation", "Budget": 175_000_000, "Revenue": 735_000_000},
    {"Title": "Inception", "Director": "Christopher Nolan", "Year": 2010, "Genre": "Sci-Fi", "Budget": 160_000_000, "Revenue": 837_000_000},
    {"Title": "Toy Story 3", "Director": "Lee Unkrich", "Year": 2010, "Genre": "Animation", "Budget": 200_000_000, "Revenue": 1_067_000_000},

    {"Title": "The Avengers", "Director": "Joss Whedon", "Year": 2012, "Genre": "Action", "Budget": 220_000_000, "Revenue": 1_519_000_000},
    {"Title": "The Hunger Games", "Director": "Gary Ross", "Year": 2012, "Genre": "Action", "Budget": 78_000_000, "Revenue": 694_000_000},
    {"Title": "Frozen", "Director": "Chris Buck and Jennifer Lee", "Year": 2013, "Genre": "Animation", "Budget": 150_000_000, "Revenue": 1_285_000_000},
    {"Title": "Gravity", "Director": "Alfonso Cuarón", "Year": 2013, "Genre": "Sci-Fi", "Budget": 100_000_000, "Revenue": 723_000_000},
    {"Title": "Interstellar", "Director": "Christopher Nolan", "Year": 2014, "Genre": "Sci-Fi", "Budget": 165_000_000, "Revenue": 733_000_000},

    {"Title": "Mad Max: Fury Road", "Director": "George Miller", "Year": 2015, "Genre": "Action", "Budget": 150_000_000, "Revenue": 380_000_000},
    {"Title": "Star Wars: The Force Awakens", "Director": "J. J. Abrams", "Year": 2015, "Genre": "Sci-Fi", "Budget": 245_000_000, "Revenue": 2_068_000_000},
    {"Title": "La La Land", "Director": "Damien Chazelle", "Year": 2016, "Genre": "Musical", "Budget": 30_000_000, "Revenue": 472_000_000},
    {"Title": "Get Out", "Director": "Jordan Peele", "Year": 2017, "Genre": "Horror", "Budget": 4_500_000, "Revenue": 255_000_000},
    {"Title": "Black Panther", "Director": "Ryan Coogler", "Year": 2018, "Genre": "Action", "Budget": 200_000_000, "Revenue": 1_349_000_000},

    {"Title": "Avengers: Endgame", "Director": "Anthony and Joe Russo", "Year": 2019, "Genre": "Action", "Budget": 356_000_000, "Revenue": 2_799_000_000},
    {"Title": "Joker", "Director": "Todd Phillips", "Year": 2019, "Genre": "Drama", "Budget": 55_000_000, "Revenue": 1_079_000_000},
    {"Title": "Dune", "Director": "Denis Villeneuve", "Year": 2021, "Genre": "Sci-Fi", "Budget": 165_000_000, "Revenue": 402_000_000},
    {"Title": "Everything Everywhere All at Once", "Director": "Daniel Kwan and Daniel Scheinert", "Year": 2022, "Genre": "Sci-Fi", "Budget": 25_000_000, "Revenue": 143_000_000},
    {"Title": "Top Gun: Maverick", "Director": "Joseph Kosinski", "Year": 2022, "Genre": "Action", "Budget": 170_000_000, "Revenue": 1_496_000_000},

    {"Title": "Avatar: The Way of Water", "Director": "James Cameron", "Year": 2022, "Genre": "Sci-Fi", "Budget": 350_000_000, "Revenue": 2_320_000_000},
    {"Title": "Barbie", "Director": "Greta Gerwig", "Year": 2023, "Genre": "Comedy", "Budget": 145_000_000, "Revenue": 1_446_000_000},
    {"Title": "Oppenheimer", "Director": "Christopher Nolan", "Year": 2023, "Genre": "Drama", "Budget": 100_000_000, "Revenue": 976_000_000},
    {"Title": "Dune: Part Two", "Director": "Denis Villeneuve", "Year": 2024, "Genre": "Sci-Fi", "Budget": 190_000_000, "Revenue": 714_000_000},
    {"Title": "Inside Out 2", "Director": "Kelsey Mann", "Year": 2024, "Genre": "Animation", "Budget": 200_000_000, "Revenue": 1_699_000_000}
]

# -----------------------------
# Initialize Data
# -----------------------------
if "movies" not in st.session_state:
    st.session_state.movies = pd.DataFrame(default_movies)

# -----------------------------
# Helper Functions
# -----------------------------
def calculate_roi(budget, revenue):
    if budget == 0:
        return 0
    return ((revenue - budget) / budget) * 100

def get_decade(year):
    return f"{year // 10 * 10}s"

def get_result_label(roi):
    if roi >= 500:
        return "Mega Hit"
    elif roi >= 300:
        return "Blockbuster"
    elif roi >= 100:
        return "Successful"
    elif roi >= 0:
        return "Moderate"
    else:
        return "Flop"

# -----------------------------
# Sidebar Add Movie
# -----------------------------
st.sidebar.header("➕ Add a New Movie")

with st.sidebar.form("add_movie_form"):
    title = st.text_input("Title")
    director = st.text_input("Director")
    year = st.number_input("Year", min_value=1900, max_value=2035, value=2024)
    genre = st.selectbox(
        "Genre",
        [
            "Action", "Adventure", "Animation", "Comedy", "Crime",
            "Drama", "Fantasy", "Horror", "Musical", "Romance",
            "Sci-Fi", "Thriller", "Other"
        ]
    )
    budget = st.number_input("Budget ($)", min_value=0, value=10_000_000, step=1_000_000)
    revenue = st.number_input("Revenue ($)", min_value=0, value=50_000_000, step=1_000_000)

    submitted = st.form_submit_button("Add Movie")

    if submitted:
        if title.strip() == "" or director.strip() == "":
            st.sidebar.error("Please enter both title and director.")
        else:
            new_movie = pd.DataFrame([
                {
                    "Title": title,
                    "Director": director,
                    "Year": int(year),
                    "Genre": genre,
                    "Budget": budget,
                    "Revenue": revenue
                }
            ])

            st.session_state.movies = pd.concat(
                [st.session_state.movies, new_movie],
                ignore_index=True
            )

            st.sidebar.success(f"{title} added successfully!")

# -----------------------------
# Prepare Data
# -----------------------------
df = st.session_state.movies.copy()
df["Profit"] = df["Revenue"] - df["Budget"]
df["ROI (%)"] = df.apply(lambda row: calculate_roi(row["Budget"], row["Revenue"]), axis=1)
df["Decade"] = df["Year"].apply(get_decade)
df["Result"] = df["ROI (%)"].apply(get_result_label)

# -----------------------------
# Sidebar Filters
# -----------------------------
st.sidebar.header("🎛️ Dashboard Options")

search_title = st.sidebar.text_input("Search movie title")

all_genres = sorted(df["Genre"].unique())
selected_genres = st.sidebar.multiselect(
    "Select genres",
    options=all_genres,
    default=all_genres
)

all_decades = sorted(df["Decade"].unique())
selected_decades = st.sidebar.multiselect(
    "Select decades",
    options=all_decades,
    default=all_decades
)

min_roi = st.sidebar.slider(
    "Minimum ROI (%)",
    min_value=int(df["ROI (%)"].min()),
    max_value=int(df["ROI (%)"].max()),
    value=int(df["ROI (%)"].min())
)

sort_option = st.sidebar.selectbox(
    "Sort movies by",
    ["Revenue", "Profit", "ROI (%)", "Budget", "Year", "Title"]
)

sort_order = st.sidebar.radio(
    "Sort order",
    ["Descending", "Ascending"]
)

max_movies = st.sidebar.slider(
    "Number of movies to display",
    min_value=5,
    max_value=len(df),
    value=min(20, len(df))
)

chart_mode = st.sidebar.selectbox(
    "Main chart type",
    [
        "Budget vs Revenue",
        "Top Profit Movies",
        "Top ROI Movies",
        "Average ROI by Genre",
        "Movie Count by Decade"
    ]
)

# -----------------------------
# Apply Filters
# -----------------------------
filtered_df = df[
    (df["Genre"].isin(selected_genres)) &
    (df["Decade"].isin(selected_decades)) &
    (df["ROI (%)"] >= min_roi)
]

if search_title.strip():
    filtered_df = filtered_df[
        filtered_df["Title"].str.contains(search_title, case=False, na=False)
    ]

ascending = True if sort_order == "Ascending" else False
filtered_df = filtered_df.sort_values(by=sort_option, ascending=ascending).head(max_movies)

# -----------------------------
# KPI Metrics
# -----------------------------
st.markdown("## 📌 Key Metrics")

if filtered_df.empty:
    st.warning("No movies match the selected filters.")
else:
    total_movies = len(filtered_df)
    total_budget = filtered_df["Budget"].sum()
    total_revenue = filtered_df["Revenue"].sum()
    total_profit = filtered_df["Profit"].sum()
    average_roi = filtered_df["ROI (%)"].mean()

    col1, col2, col3, col4, col5 = st.columns(5)

    col1.metric("Movies", f"{total_movies}")
    col2.metric("Total Budget", f"${total_budget:,.0f}")
    col3.metric("Total Revenue", f"${total_revenue:,.0f}")
    col4.metric("Total Profit", f"${total_profit:,.0f}")
    col5.metric("Average ROI", f"{average_roi:.2f}%")

    # -----------------------------
    # Main Chart
    # -----------------------------
    st.markdown("## 📊 Main Visualization")

    if chart_mode == "Budget vs Revenue":
        chart_df = filtered_df.melt(
            id_vars="Title",
            value_vars=["Budget", "Revenue"],
            var_name="Category",
            value_name="Amount"
        )

        fig = px.bar(
            chart_df,
            x="Title",
            y="Amount",
            color="Category",
            barmode="group",
            title="Budget vs Revenue by Movie",
            labels={"Amount": "Amount ($)", "Title": "Movie"}
        )

    elif chart_mode == "Top Profit Movies":
        chart_df = filtered_df.sort_values(by="Profit", ascending=False)
        fig = px.bar(
            chart_df,
            x="Title",
            y="Profit",
            title="Top Movies by Profit",
            labels={"Profit": "Profit ($)", "Title": "Movie"}
        )

    elif chart_mode == "Top ROI Movies":
        chart_df = filtered_df.sort_values(by="ROI (%)", ascending=False)
        fig = px.bar(
            chart_df,
            x="Title",
            y="ROI (%)",
            title="Top Movies by ROI",
            labels={"ROI (%)": "ROI (%)", "Title": "Movie"}
        )

    elif chart_mode == "Average ROI by Genre":
        chart_df = filtered_df.groupby("Genre", as_index=False)["ROI (%)"].mean()
        fig = px.bar(
            chart_df,
            x="Genre",
            y="ROI (%)",
            title="Average ROI by Genre",
            labels={"ROI (%)": "Average ROI (%)", "Genre": "Genre"}
        )

    else:
        chart_df = filtered_df["Decade"].value_counts().reset_index()
        chart_df.columns = ["Decade", "Count"]
        fig = px.bar(
            chart_df,
            x="Decade",
            y="Count",
            title="Movie Count by Decade",
            labels={"Count": "Number of Movies", "Decade": "Decade"}
        )

    fig.update_layout(height=520)
    st.plotly_chart(fig, use_container_width=True)

    # -----------------------------
    # Secondary Charts
    # -----------------------------
    st.markdown("## 🧭 Additional Analysis")

    col_a, col_b = st.columns(2)

    with col_a:
        genre_counts = filtered_df["Genre"].value_counts().reset_index()
        genre_counts.columns = ["Genre", "Count"]

        pie_chart = px.pie(
            genre_counts,
            names="Genre",
            values="Count",
            title="Genre Distribution"
        )
        st.plotly_chart(pie_chart, use_container_width=True)

    with col_b:
        result_counts = filtered_df["Result"].value_counts().reset_index()
        result_counts.columns = ["Result", "Count"]

        result_chart = px.bar(
            result_counts,
            x="Result",
            y="Count",
            title="Movie Performance Categories",
            labels={"Count": "Number of Movies", "Result": "Performance Result"}
        )
        st.plotly_chart(result_chart, use_container_width=True)

    # -----------------------------
    # Data Table
    # -----------------------------
    st.markdown("## 📋 Movie Data Table")

    display_df = filtered_df.copy()
    display_df["Budget"] = display_df["Budget"].map("${:,.0f}".format)
    display_df["Revenue"] = display_df["Revenue"].map("${:,.0f}".format)
    display_df["Profit"] = display_df["Profit"].map("${:,.0f}".format)
    display_df["ROI (%)"] = display_df["ROI (%)"].map("{:.2f}%".format)

    st.dataframe(display_df, use_container_width=True)

    # -----------------------------
    # Insight Text
    # -----------------------------
    st.markdown("## 📝 Quick Insight")

    best_roi_movie = filtered_df.sort_values(by="ROI (%)", ascending=False).iloc[0]
    highest_revenue_movie = filtered_df.sort_values(by="Revenue", ascending=False).iloc[0]
    most_profitable_movie = filtered_df.sort_values(by="Profit", ascending=False).iloc[0]

    st.success(
        f"""
        Among the selected movies, **{best_roi_movie['Title']}** has the highest ROI,
        **{highest_revenue_movie['Title']}** has the highest revenue,
        and **{most_profitable_movie['Title']}** has the highest profit.
        """
    )

# -----------------------------
# Reset Button
# -----------------------------
st.divider()

if st.button("Reset to Default Movies"):
    st.session_state.movies = pd.DataFrame(default_movies)
    st.success("Dashboard reset to default movie data.")
    st.rerun()

st.caption(
    "Note: Movie budget and revenue values are approximate sample data for educational dashboard purposes."
)
