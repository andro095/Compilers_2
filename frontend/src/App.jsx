import { useState } from 'react';
import { MyEditor, Options } from './components';
import { useExecute } from './hooks/useExecute';
import Editor from "@monaco-editor/react";

export const App = () => {

    const [program, setProgram] = useState('');

    const { onExecute, msgs, intercode} = useExecute();

   

    return (
        <div className='flex flex-column w-full overflow-hidden h-screen'>
            <h2 className='text-center text-6xl font-bold m-4'>Yaplide</h2>
            <div className='flex-grow-1 flex'>
            <Options setProgram={ setProgram } onExecute={ () => onExecute(program) }/>

            <MyEditor program={ program } setProgram={ setProgram } msgs={ msgs } />

            <div className='w-4 mx-2 mb-2 border-round overflow-hidden flex flex-column'>
                <Editor
                    height="100%"
                    width="100%"
                    defaultValue="-- Aqui aparece el codigo intermedio"
                    className='shadow-4'
                    value={ intercode }
                    options={{readOnly: true}}
                />
            </div>
                
            </div>

        </div>
    )
}
