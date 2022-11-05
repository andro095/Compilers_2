import { useState } from "react";

import axios from "axios";


export const useExecute = () => {

    const [msgs, setMsgs] = useState([]);
    const [intercode, setIntercode] = useState('');
    const [objCode, setObjCode] = useState('');

    const onCompile = (program) => {

        axios.post("/compile", { code: program })
            .then(res => {
                setMsgs(res.data.messages);
                setIntercode(res.data.intercode);
                setObjCode(res.data.obj_code);
            });
    }

    return {
        onCompile,
        msgs,
        intercode,
        objCode
    };
}