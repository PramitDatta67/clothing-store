import streamlit as st

# Sample product data
products = [
    {
        "name": "BGMI Meme Tee",
        "price": 499,
        "image": "https://i.imgur.com/lD3tG7s.png"  # Replace with your image
    },
    {
        "name": "Anime Oversized Tee",
        "price": 599,
        "image": "https://i.imgur.com/LK1u2ob.png"  # Replace with your image
    },
    {
        "name": "Classic Meme Tee",
        "price": 449,
        "image": "https://i.imgur.com/tGHtX3G.png"  # Replace with your image
    }
]

# Page setup
st.set_page_config(page_title="Nice Clothing Store", layout="wide")
st.title("🛍️ Nice Clothing Store")
st.markdown("##### Meme, Anime & BGMI-themed T-Shirts — Print-on-Demand")

# Cart initialization
if "cart" not in st.session_state:
    st.session_state.cart = []

# Display products
cols = st.columns(3)
for i, product in enumerate(products):
    with cols[i]:
        st.image(product["image"], use_column_width=True)
        st.markdown(f"**{product['name']}**")
        st.markdown(f"💸 ₹{product['price']}")
        if st.button("Add to Cart", key=f"btn_{i}"):
            st.session_state.cart.append(product)
            st.success(f"✅ {product['name']} added to cart")

# Divider
st.markdown("---")
st.subheader("🛒 Your Cart")

# Display cart
total = 0
if st.session_state.cart:
    for item in st.session_state.cart:
        st.markdown(f"- {item['name']} - ₹{item['price']}")
        total += item["price"]
    st.markdown(f"**Total: ₹{total}**")
else:
    st.info("Your cart is empty.")

# Checkout
if st.button("🚀 Proceed to Checkout"):
    st.warning("This is a demo. Add payment or print-on-demand API here.")
