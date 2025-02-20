import React, { useEffect, useState } from "react";
import { getSuppliers } from "../api";

const SupplierPage = () => {
    const [suppliers, setSuppliers] = useState([]);
    const [error, setError] = useState("");

    useEffect(() => {
        getSuppliers()
            .then(setSuppliers)
            .catch((error) => setError(error.message));
    }, []);

    return (
        <div>
            <h2>Supplier List</h2>
            {error ? (
                <p style={{ color: "red" }}>{error}</p>
            ) : (
                <ul>
                    {suppliers.map((supplier) => (
                        <li key={supplier.id}>
                            {supplier.name} - Compliance Score: {supplier.compliance_score}%
                        </li>
                    ))}
                </ul>
            )}
        </div>
    );
};

export default SupplierPage;
