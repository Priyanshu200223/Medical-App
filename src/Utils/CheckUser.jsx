import { useEffect, useState } from "react";
import axios from "axios";

const useUserRole = () => {
  const [userRole, setUserRole] = useState(null);

  useEffect(() => {
    const checkUserRole = async () => {
      try {
        const response = await axios.get(
          "https://medi-dep-bykw.vercel.app/check/",
          {
            headers: {
              Authorization: `Bearer ${localStorage.getItem("access_token")}`,
            },
          }
        );
        setUserRole(response.data.role);
      } catch (error) {
        console.error("Error checking user role:", error);
      }
    };

    checkUserRole();
  }, []);

  return userRole;
};

export default useUserRole;