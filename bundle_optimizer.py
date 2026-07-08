import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from scipy.optimize import linprog

# ==============================================================================
# 1. SYNTHETIC CUSTOMER DATA GENERATION
# ==============================================================================
def generate_subscriber_data(n_samples=5000):
    """
    Generates user streaming metrics mapping to the 4 strategic personas:
    Budget Student, Family Household, Urban Professional, Emerging Market Viewer
    """
    np.random.seed(42)
    
    # Features: [Price Sensitivity (0-1), Viewing Hours/Mo, Shared Profiles, Local Content Ratio]
    student = np.random.multivariate_normal([0.9, 25, 1.2, 0.2], [[0.01, 2, 0.1, 0.01], [2, 10, 0.1, 1], [0.1, 0.1, 0.1, 0.01], [0.01, 1, 0.01, 0.05]], int(n_samples * 0.15))
    family = np.random.multivariate_normal([0.5, 80, 4.5, 0.4], [[0.02, 5, 0.3, 0.02], [5, 40, 0.5, 2], [0.3, 0.5, 0.5, 0.05], [0.02, 2, 0.05, 0.05]], int(n_samples * 0.25))
    urban_pro = np.random.multivariate_normal([0.2, 35, 1.5, 0.1], [[0.01, 3, 0.2, 0.01], [3, 15, 0.2, 1], [0.2, 0.2, 0.2, 0.01], [0.01, 1, 0.01, 0.02]], int(n_samples * 0.20))
    emerging = np.random.multivariate_normal([0.8, 50, 2.5, 0.85], [[0.01, 4, 0.2, 0.01], [4, 25, 0.3, 1], [0.2, 0.3, 0.3, 0.02], [0.01, 1, 0.02, 0.02]], int(n_samples * 0.40))
    
    data = np.vstack([student, family, urban_pro, emerging])
    df = pd.DataFrame(data, columns=['price_sensitivity', 'viewing_hours', 'profile_count', 'local_content_ratio'])
    
    df['price_sensitivity'] = df['price_sensitivity'].clip(0, 1)
    df['viewing_hours'] = df['viewing_hours'].clip(0, 200)
    df['profile_count'] = df['profile_count'].clip(1, 6).round().astype(int)
    df['local_content_ratio'] = df['local_content_ratio'].clip(0, 1)
    
    return df

# ==============================================================================
# 2. MACHINE LEARNING ENGINE: PERSONA SEGMENTATION
# ==============================================================================
def segment_subscribers(df):
    """
    Applies Feature Scaling and K-Means clustering to discover and tag user personas.
    """
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(df)
    
    kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
    df['persona_cluster'] = kmeans.fit_predict(scaled_features)
    
    cluster_means = df.groupby('persona_cluster').mean()
    persona_mapping = {}
    for cluster_id, row in cluster_means.iterrows():
        if row['price_sensitivity'] > 0.7 and row['local_content_ratio'] > 0.6:
            persona_mapping[cluster_id] = "Emerging Market Viewer"
        elif row['price_sensitivity'] > 0.7:
            persona_mapping[cluster_id] = "Budget Student"
        elif row['profile_count'] > 3.0:
            persona_mapping[cluster_id] = "Family Household"
        else:
            persona_mapping[cluster_id] = "Urban Professional"
            
    df['persona_name'] = df['persona_cluster'].map(persona_mapping)
    return df, kmeans

# ==============================================================================
# 3. MATHEMATICAL OPTIMIZATION FRAMEWORK (SciPy)
# ==============================================================================
def optimize_bundle_allocation():
    """
    Linear Programming execution using SciPy Optimize.
    Objective: Maximize Incremental Revenue contribution ($4.8B target).
    Constraints: Adhere strictly to the $1.5B investment allocation cap.
    """
    print("\n--- Running Mathematical Revenue Optimization Framework ---")
    
    # Coefficients for the Objective Function (Negative values for maximization)
    c = [-1.8, -2.1, -0.9] 
    
    # Inequality Constraint Matrix (A_ub * x <= b_ub) -> Investment constraint
    A = [[0.6, 0.7, 0.2]]
    b = [1.5]
    
    x_bounds = [(0, 2), (0, 2), (0, 2)]
    result = linprog(c, A_ub=A, b_ub=b, bounds=x_bounds, method='highs')
    
    if result.success:
        print(f"Optimization Status: Optimal Portfolio Allocated Successfully.")
        print(f"Allocated Intensity Multipliers -> AI Bundles: {result.x[0]:.2f}x | Regional Expansion: {result.x[1]:.2f}x | Tier Pricing: {result.x[2]:.2f}x")
        print(f"Maximized Optimized Strategic Value Generation: ${(-result.fun):.2f}B")
    else:
        print("Optimization convergence failed to find an allocation.")

# ==============================================================================
# 4. EXECUTION PIPELINE
# ==============================================================================
if __name__ == "__main__":
    print("Initializing Subscription Analytics Engine...")
    raw_data = generate_subscriber_data(n_samples=10000)
    processed_data, model = segment_subscribers(raw_data)
    
    print("\n--- Identified Demographics Summary ---")
    print(processed_data['persona_name'].value_counts(normalize=True).to_string())
    
    optimize_bundle_allocation()
