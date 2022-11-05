import { useEffect, useState } from 'react';
import { MyCodes, MyEditor, Options } from './components';
import { useExecute } from './hooks/useExecute';
import { useSave } from './hooks/useSave';

export const App = () => {

    const [program, setProgram] = useState('');

    const [isCodeGenerated, setIsCodeGenerated] = useState(false);

    const { onCompile, msgs, intercode, objCode } = useExecute();

    const { onSave, setFileName, fileName } = useSave();

    useEffect(() => {
        if (intercode !== '') {
            setIsCodeGenerated(true);
        }

    }, [intercode])
    

    return (
        <div className='flex flex-column w-full overflow-hidden h-full'>
            <h2 className='text-center text-6xl font-bold m-4'>Yaplide</h2>
            <div className='flex-grow-1 flex'>
                <Options 
                        setProgram={ setProgram } 
                        onCompile = { () => onCompile(program) } 
                        onSave={ onSave }
                        fileName={ fileName }
                        setFileName={ setFileName }
                        isCodeGenerated={ isCodeGenerated }
                />

                <MyEditor program={ program } setProgram={ setProgram } msgs={ msgs } />

                <MyCodes intercode={ intercode } obj_code={ objCode } />
            </div>

        </div>
    )
}
