import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# ==========================================
# PART 1: SETUP
# ==========================================
print("🔄 Generating Sales Data...")
np.random.seed(42)
rows = 1500

# Consulting Dimensions
regions = ['North America', 'Europe', 'APAC', 'LATAM']
services = ['Strategy Consulting', 'Tech Implementation', 'Risk Advisory', 'Audit Services']
industries = ['Finance', 'Healthcare', 'Retail', 'Government', 'Energy']

# ==========================================
# PART 2: GENERATE REALISTIC TRANSACTIONS
# ==========================================
data = []
start_date = datetime(2024, 1, 1)

for i in range(rows):
    # Random Date (Last 2 Years)
    date = start_date + timedelta(days=random.randint(0, 730))
    
    region = random.choice(regions)
    service = random.choice(services)
    industry = random.choice(industries)
    
    # LOGIC: Strategy pays more, Audit pays less
    base_sales = random.randint(5000, 80000)
    
    if service == 'Strategy Consulting':
        sales = base_sales * 1.5
        # Strategy has higher margins (50-70%)
        margin_pct = random.uniform(0.50, 0.70) 
    elif service == 'Audit Services':
        sales = base_sales * 0.8
        # Audit has tight margins (10-25%)
        margin_pct = random.uniform(0.10, 0.25)
    else:
        sales = base_sales
        margin_pct = random.uniform(0.25, 0.45)
        
    cost = sales * (1 - margin_pct)
    profit = sales - cost
    
    data.append([date, region, service, industry, int(sales), int(cost), int(profit)])

# ==========================================
# PART 3: SAVE TO CSV
# ==========================================
df = pd.DataFrame(data, columns=['Date', 'Region', 'Service_Line', 'Industry', 'Revenue', 'Cost', 'Profit'])

# Add "Quarter" for trend analysis
df['Quarter'] = df['Date'].apply(lambda x: f"Q{(x.month-1)//3 + 1}-{x.year}")

df.to_csv('consulting_sales_data.csv', index=False)
print("✅ Success! Data saved as 'consulting_sales_data.csv'")
print(f"   - Total Records: {len(df)}")
print(f"   - Total Revenue Generated: ${df['Revenue'].sum():,}")