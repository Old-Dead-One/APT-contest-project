const API_BASE_URL = "./backend/main_player.py";

export const getCart = async () => {
  try {
    const response = await fetch(`${API_BASE_URL}/cart/`);
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
    return await response.json();
  } catch (error) {
    console.error("Error fetching cart:", error);
    throw error;
  }
};

export const addToCart = async (cart) => {
  try {
    const response = await fetch(`${API_BASE_URL}/cart/`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(cart),
    });
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
    return await response.json();
  } catch (error) {
    console.error("Error adding to cart:", error);
    throw error;
  }
};

export const removeFromCart = async (cart) => {
  try {
    const response = await fetch(`${API_BASE_URL}/cart/${cart.id}`, {
      method: "DELETE",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(cart),
    });
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
    return await response.json();
  } catch (error) {
    console.error("Error removing from cart:", error);
    throw error;
  }
};

export const updateCart = async (cart) => {
  try {
    const response = await fetch(`${API_BASE_URL}/cart/${cart.id}`, {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(cart),
    });
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
    return await response.json();
  } catch (error) {
    console.error("Error updating cart:", error);
    throw error;
  }
};

export const deleteCart = async (cartId) => {
  try {
    const response = await fetch(`${API_BASE_URL}/cart/${cartId}`, {
      method: "DELETE",
    });
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
  } catch (error) {
    console.error("Error deleting cart:", error);
    throw error;
  }
};

export const clearCart = async () => {
  try {
    const response = await fetch(`${API_BASE_URL}/cart/`, {
      method: "DELETE",
    });
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
  } catch (error) {
    console.error("Error clearing cart:", error);
    throw error;
  }
};

export const checkoutCart = async () => {
  try {
    const response = await fetch(`${API_BASE_URL}/cart/checkout`, {
      method: "POST",
    });
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
  } catch (error) {
    console.error("Error checking out cart:", error);
    throw error;
  }
};

export const getCartTotal = async () => {
  try {
    const response = await fetch(`${API_BASE_URL}/cart/total`);
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
    return await response.json();
  } catch (error) {
    console.error("Error fetching cart total:", error);
    throw error;
  }
};

export const getCartCount = async () => {
  try {
    const response = await fetch(`${API_BASE_URL}/cart/count`);
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
    return await response.json();
  } catch (error) {
    console.error("Error fetching cart count:", error);
    throw error;
  }
};

export const getCartItems = async () => {
  try {
    const response = await fetch(`${API_BASE_URL}/cart/items`);
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
    return await response.json();
  } catch (error) {
    console.error("Error fetching cart items:", error);
    throw error;
  }
};
