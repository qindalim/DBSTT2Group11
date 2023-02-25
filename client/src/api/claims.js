import axios from "axios";

export const getClaims = async () => {


    axios.get('http://localhost:5000/getData/58001001')
        .then(response => {
            const data = response.data.data.claims
            let toReturn = []
            for (const [index, element] of data.entries()) {
                element["id"] = index
                toReturn.push(element)
            }
            console.log(toReturn)
            return toReturn
        })
        .catch(er => {
            console.log(er)
        })

}

