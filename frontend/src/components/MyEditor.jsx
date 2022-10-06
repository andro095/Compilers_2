import Editor from "@monaco-editor/react";
import PropTypes from 'prop-types';

import { MyConsole } from "./";

export const MyEditor = ({ program, setProgram, msgs=[] }) => {
    return (
        <div className='flex-grow-1 flex mx-2 mb-2 border-round overflow-hidden flex flex-column'>
            <Editor
                height="75%"
                width="100%"
                defaultValue="-- Escriba aqui su codigo"
                className='shadow-4'
                value={ program }
                onChange={ setProgram }
            />
            <MyConsole msgs={ msgs } />
        </div>
    )
}

MyEditor.propTypes = {
    program: PropTypes.string.isRequired,
    setProgram: PropTypes.func.isRequired
}
