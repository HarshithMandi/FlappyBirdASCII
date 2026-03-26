
import React, { useState, useEffect } from 'react';
import { getProducts } from '../api/api';

const ProductList = () => {
    const [products, setProducts] = useState([]);

    useEffect(() => {
        const fetchProducts = async () => {
            try {
                const data = await getProducts();  // Assuming `data` is an array of products
                setProducts(data);  // Update state with the fetched products
            } catch (error) {
                console.error('Failed to fetch products', error);
            }
        };
        fetchProducts();
    }, []);

    return (
        <div>
            <h1>Product List</h1>
            {
                products.length === 0 ? (
                    <p>No products available</p>
                ) : (
                    products.map((product) => (
                        <div key={product.id}>
                            <h2>{product.name}</h2>
                            <p>Price: {product.price}</p>
                            <p>Category: {product.category}</p>
                        </div>
                    ))
                )
            }
        </div>
    );
};

export default ProductList;
