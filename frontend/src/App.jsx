import { useState } from 'react';
import { MyEditor, Options } from './components';
import { useExecute } from './hooks/useExecute';

export const App = () => {

    const [program, setProgram] = useState('');

    const { onExecute, msgs} = useExecute();

   

    return (
        <div className='flex flex-column w-full overflow-hidden h-screen'>
            <h2 className='text-center text-6xl font-bold m-4'>Yaplide</h2>
            <div className='flex-grow-1 flex'>
            <Options setProgram={ setProgram } onExecute={ () => onExecute(program) }/>

            <MyEditor program={ program } setProgram={ setProgram } msgs={ msgs } />

            
            </div>

        </div>
    )
}
