import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Navbar from "./components/Navbar";
import SupplierList from "./pages/SupplierPage";
import CompliancePage from "./pages/CompliancePage";
import InsightsPage from "./pages/InsightsPage";
import Home from "./pages/Home";
import "./styles/styles.css";

function App() {
    return (
        <Router>
            <Navbar />
            <div className="container">
                <Routes>
                    <Route path="/" element={<Home />} />
                    <Route path="/suppliers" element={<SupplierList />} />
                    <Route path="/compliance" element={<CompliancePage />} />
                    <Route path="/insights" element={<InsightsPage />} />
                </Routes>
            </div>
        </Router>
    );
}

export default App;
