import { useEffect, useState } from "react"
import { ConsoleMessage } from "./ConsoleMessage"

export const MyConsole = ({ msgs = [] }) => {

    const [messages, setMessages] = useState([])

    useEffect(() => {
        setMessages(msgs)
    }, [])
    


    return (
        <div className="border-round border-1 border-900 h-13rem surface-ground mt-2 p-2 flex flex-column overflow-x-hidden overflow-y-auto">
            {
                messages.map((m, index) => <ConsoleMessage key={index} type={m.type} msg={m.msg}/>)
            }
        </div>
    )
}
