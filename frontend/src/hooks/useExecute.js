import { useState } from "react";

import axios from "axios";


export const useExecute = () => {

    const [msgs, setMsgs] = useState([]);

    const onExecute = (program) => {

        axios.post("/execute", { code: program })
            .then(res => {
                setMsgs(res.data.messages);
            });
    }

    return {
        onExecute,
        msgs
    };
}