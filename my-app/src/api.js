import axios from "axios";

const BASE_URL = "http://127.0.0.1:8000";

// Fetch all suppliers
export const getSuppliers = async () => {
    try {
        const response = await axios.get(`${BASE_URL}/suppliers`);
        return response.data;
    } catch (error) {
        console.error("Error fetching suppliers:", error);
        throw error;
    }
};

// Fetch supplier insights (AI-based)
export const getInsights = async () => {
    try {
        const response = await axios.get(`${BASE_URL}/suppliers/insights`);
        return response.data.insights;
    } catch (error) {
        console.error("Error fetching insights:", error);
        throw error;
    }
};

// Fetch compliance data
export const getComplianceData = async () => {
    try {
        const response = await axios.get(`${BASE_URL}/compliance-data`);
        return response.data;
    } catch (error) {
        console.error("Error fetching compliance data:", error);
        throw error;
    }
};

// Check supplier compliance using AI
export const checkCompliance = async (record) => {
    try {
        const response = await axios.post(`${BASE_URL}/suppliers/check-compliance`, record);
        return response.data;
    } catch (error) {
        console.error("Error checking compliance:", error);
        throw error;
    }
};
