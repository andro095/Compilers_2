import { useState } from "react";

import axios from "axios";


export const useExecute = () => {

    const [msgs, setMsgs] = useState([]);
    const [intercode, setIntercode] = useState('');

    const onExecute = (program) => {

        axios.post("/execute", { code: program })
            .then(res => {
                setMsgs(res.data.messages);
                setIntercode(res.data.intercode);
            });
    }

    return {
        onExecute,
        msgs,
        intercode,
    };
}