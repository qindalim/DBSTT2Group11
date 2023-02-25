import axios from "axios";

export const getClaims = async () => {
    let response = axios.get('https://localhost:3000/home')
    return response;
}

