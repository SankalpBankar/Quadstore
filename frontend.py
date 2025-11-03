import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="QuadStore 🛒", layout="wide")
st.title("🛒 QuadStore – Product Management System")

menu = ["View Products", "Add Product", "Update Product", "Delete Product"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "View Products":
    st.subheader("📋 All Products")
    response = requests.get(f"{API_URL}/products/")
    if response.status_code == 200:
        data = response.json()
        if data:
            for prod in data:
                with st.expander(f"{prod['name']} – ₹{prod['price']}"):
                    st.write(prod["description"])
        else:
            st.info("No products found.")
    else:
        st.error("Failed to fetch products")

elif choice == "Add Product":
    st.subheader("➕ Add a New Product")
    name = st.text_input("Product Name")
    price = st.number_input("Price", min_value=0.0)
    desc = st.text_area("Description")
    if st.button("Add Product"):
        payload = {"name": name, "price": price, "description": desc}
        res = requests.post(f"{API_URL}/products/", json=payload)
        if res.status_code == 200:
            st.success("Product added successfully ✅")
        else:
            st.error("Error adding product")

elif choice == "Update Product":
    st.subheader("✏️ Update Product")
    pid = st.number_input("Product ID", min_value=1)
    name = st.text_input("New Name")
    price = st.number_input("New Price", min_value=0.0)
    desc = st.text_area("New Description")
    if st.button("Update"):
        payload = {"name": name, "price": price, "description": desc}
        res = requests.put(f"{API_URL}/products/{pid}", json=payload)
        if res.status_code == 200:
            st.success("Product updated successfully ✅")
        else:
            st.error("Product not found ❌")

elif choice == "Delete Product":
    st.subheader("🗑️ Delete Product")
    pid = st.number_input("Enter Product ID to Delete", min_value=1)
    if st.button("Delete"):
        res = requests.delete(f"{API_URL}/products/{pid}")
        if res.status_code == 200:
            st.success("Product deleted ✅")
        else:
            st.error("Product not found ❌")
