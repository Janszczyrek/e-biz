import React, { useState, useEffect } from "react";
import Cookies from "js-cookie";
import { useNavigate } from "react-router-dom";

function Logout({ onLogoutSuccess }) {
    const [error, setError] = useState("");
    const navigate = useNavigate();

    const handleLogout = async () => {
        try {
            const response = await fetch("http://localhost:5000/auth/logout", {
                method: "POST",
                credentials: "include",
            });
            if (response.ok) {
                Cookies.remove("user_id", { path: '/' });
                Cookies.remove("username", { path: '/' });
                navigate('/', { replace: true });
                onLogoutSuccess();
            } else {
                const errorData = await response.json();
                setError(errorData.message || "Logout failed");
            }
        } catch (err) {
            setError("An error occurred during logout.");
            console.error("Logout error:", err);
        }
    };

    useEffect(() => {
        handleLogout();
    }, []);

    if (error) {
        return <div>Error: {error}</div>;
    }
}
export default Logout;