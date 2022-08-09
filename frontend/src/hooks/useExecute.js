import { useState } from "react";

import axios from "axios";


export const useExecute = () => {

    const [msgs, setMsgs] = useState([]);

    const onExecute = (program) => {

        axios.post("/execute", { code: program })
            .then(res => {
                console.log(res.data);
            });
        // console.log(program);
    }

    return {
        onExecute,
        msgs
    };
}