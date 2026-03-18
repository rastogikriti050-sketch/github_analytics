import streamlit as st
import requests
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="GitHub Analytics Dashboard", page_icon="🚀", layout="wide")

st.title("🚀 GitHub User Analytics Dashboard")

username = st.text_input("Enter GitHub Username")

if username:
    user_url = f"https://api.github.com/users/{username}"
    repos_url = f"https://api.github.com/users/{username}/repos"

    user_res = requests.get(user_url)
    repos_res = requests.get(repos_url)

    if user_res.status_code != 200:
        st.error("User not found!")
    else:
        user_data = user_res.json()
        repos_data = repos_res.json()

        # --- USER INFO ---
        st.markdown("## 👤 User Overview")

        col1, col2, col3 = st.columns(3)
        col1.metric("📦 Repos", user_data['public_repos'])
        col2.metric("👥 Followers", user_data['followers'])
        col3.metric("➡️ Following", user_data['following'])

        if repos_data:
            df = pd.DataFrame(repos_data)

            # --- PREPROCESS ---
            df['created_at'] = pd.to_datetime(df['created_at'])

            # --- KEY INSIGHTS ---
            total_stars = df['stargazers_count'].sum()
            total_forks = df['forks_count'].sum()

            df_sorted = df.sort_values(by='stargazers_count', ascending=False).head(10)

            st.markdown("## ⭐ Key Insights")

            col4, col5, col6 = st.columns(3)

            if not df_sorted.empty:
                col4.metric("🔥 Top Repo", df_sorted.iloc[0]['name'])
            else:
                col4.metric("🔥 Top Repo", "N/A")

            col5.metric("⭐ Total Stars", total_stars)
            col6.metric("🍴 Total Forks", total_forks)

            # --- LANGUAGE DISTRIBUTION ---
            st.markdown("## 🧠 Language Distribution")

            lang_count = df['language'].value_counts().dropna().reset_index()
            lang_count.columns = ['Language', 'Count']

            fig1 = px.pie(lang_count, names='Language', values='Count')
            st.plotly_chart(fig1, use_container_width=True)

            # --- PERFORMANCE ---
            st.markdown("## 📊 Repository Performance")

            col7, col8 = st.columns(2)

            fig2 = px.bar(
                df_sorted,
                x='name',
                y='stargazers_count',
                title="⭐ Stars"
            )
            col7.plotly_chart(fig2, use_container_width=True)

            fig3 = px.bar(
                df_sorted,
                x='name',
                y='forks_count',
                title="🍴 Forks"
            )
            col8.plotly_chart(fig3, use_container_width=True)

            # --- TIMELINE ---
            st.markdown("## 📈 Activity Timeline")

            timeline = df.groupby(df['created_at'].dt.year).size().reset_index(name='repos')

            fig4 = px.line(
                timeline,
                x='created_at',
                y='repos',
                markers=True,
                title="Repositories Created Over Time"
            )
            st.plotly_chart(fig4, use_container_width=True)

            # --- HEATMAP ---
            st.markdown("## 🔥 Activity Heatmap")

            df['day'] = df['created_at'].dt.day
            df['month'] = df['created_at'].dt.month

            heatmap_data = df.groupby(['month', 'day']).size().reset_index(name='count')

            fig_heatmap = px.density_heatmap(
                heatmap_data,
                x='day',
                y='month',
                z='count',
                color_continuous_scale='greens',
                title="Repository Activity Heatmap"
            )

            st.plotly_chart(fig_heatmap, use_container_width=True)

        else:
            st.warning("No repositories found for this user.")