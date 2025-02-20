import { useState, useEffect } from "react";

function InsightsPage() {
  const [insights, setInsights] = useState([]);

  useEffect(() => {
    fetch("http://localhost:8000/suppliers/insights")
      .then((res) => res.json())
      .then((data) => {
        // Ensure insights is always an array
        if (Array.isArray(data.insights)) {
          setInsights(data.insights);
        } else {
          setInsights([]); // Set empty array if the response is not an array
        }
      })
      .catch((error) => console.error("Error fetching insights:", error));
  }, []);

  return (
    <div>
      <h2>Supplier Insights</h2>
      {insights.length === 0 ? (
        <p>No insights available.</p>
      ) : (
        <ul>
          {insights.map((insight, index) => (
            <li key={index}>{insight}</li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default InsightsPage;
