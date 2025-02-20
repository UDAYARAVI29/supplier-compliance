import React, { useState } from "react";
import { checkCompliance } from "../api";

const CompliancePage = () => {
    const [formData, setFormData] = useState({
        supplier_id: "",
        metric: "",
        date_recorded: "",
        result: "",
        status: "",
    });

    const [responseMessage, setResponseMessage] = useState("");
    const [error, setError] = useState("");

    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await checkCompliance(formData);
            setResponseMessage(response.message);
        } catch (error) {
            setError(error.message);
        }
    };

    return (
        <div>
            <h2>Submit Compliance Data</h2>
            <form onSubmit={handleSubmit}>
                <label>Supplier ID:</label>
                <input type="number" name="supplier_id" value={formData.supplier_id} onChange={handleChange} required />

                <label>Metric:</label>
                <input type="text" name="metric" value={formData.metric} onChange={handleChange} required />

                <label>Date Recorded:</label>
                <input type="date" name="date_recorded" value={formData.date_recorded} onChange={handleChange} required />

                <label>Result:</label>
                <input type="text" name="result" value={formData.result} onChange={handleChange} required />

                <label>Status:</label>
                <select name="status" value={formData.status} onChange={handleChange} required>
                    <option value="">Select</option>
                    <option value="Compliant">Compliant</option>
                    <option value="Non-compliant">Non-compliant</option>
                </select>

                <button type="submit">Submit</button>
            </form>

            {responseMessage && <p style={{ color: "green" }}>{responseMessage}</p>}
            {error && <p style={{ color: "red" }}>{error}</p>}
        </div>
    );
};

export default CompliancePage;
