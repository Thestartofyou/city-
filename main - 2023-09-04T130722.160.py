import pandas as pd
import matplotlib.pyplot as plt

# Simulated data for new business registrations (replace with actual data source)
data = {
    'City': ['Medford', 'Woburn', 'Melrose', 'Wakefield', 'Reading', 'Malden', 'Winchester', 'Lynnfield', 'Saugus', 'Burlington'],
    'Year': [2023, 2023, 2023, 2023, 2023, 2023, 2023, 2023, 2023, 2023],
    'NewBusinessCount': [20, 15, 10, 12, 18, 14, 8, 10, 9, 16]
}

# Create a DataFrame from the data
business_data = pd.DataFrame(data)

# Group the data by city and calculate the total new business count
city_growth = business_data.groupby('City')['NewBusinessCount'].sum().reset_index()

# Sort the cities by new business count
city_growth = city_growth.sort_values(by='NewBusinessCount', ascending=False)

# Data Visualization
plt.figure(figsize=(10, 6))
plt.bar(city_growth['City'], city_growth['NewBusinessCount'])
plt.title('New Business Growth in Cities')
plt.xlabel('City')
plt.ylabel('Total New Businesses')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
