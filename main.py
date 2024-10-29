cameras = {
    "laptop": {
        "source": 1,
        "features": ["face", "person", "object"]
    }
}

laptop_source = cameras["laptop"]["source"]
laptop_features = cameras["laptop"]["features"]

print(f"Laptop camera source: {laptop_source}")
print(f"Laptop camera features: {laptop_features}")
