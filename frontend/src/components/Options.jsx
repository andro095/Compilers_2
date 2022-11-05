import PropTypes from 'prop-types';

import { FileUpload } from 'primereact/fileupload';
import { Button } from 'primereact/button';
import { InputText } from 'primereact/inputtext';

export const Options = ({ setProgram, onCompile, onSave, fileName, setFileName, isCodeGenerated }) => {

    const onUploadFile = ({ files }) => {
        const reader = new FileReader();
        reader.onload = (e) => {
            const text = e.target.result;
            setProgram(text);
        }
        reader.readAsText(files[0]);
    }

    return (
        <div
            className='bg-white mt-8 card h-fit-content border-round w-2 shadow-4 ml-2 mr-2 flex flex-column align-items-center'
        >
            <h2 className='text-center text-4xl text-900 mb-0'>Opciones</h2>
            <p className=''>Sube tu archivo:</p>
            <FileUpload
                auto
                accept='.yapl' 
                className='mx-3'
                mode='basic' 
                name="uploader" 
                url='./upload'
                onSelect={ onUploadFile }
                chooseLabel='Seleccionar'
                />
            <Button 
                label='Compilar' 
                className='p-button-rounded mt-4 mb-5 p-button-success' 
                onClick={ onCompile }
            />

            {
                isCodeGenerated && <>
                    <span className="p-float-label">
                        <InputText 
                                className='border-round-3xl'
                                id="username" 
                                value={fileName} 
                                onChange={(e) => setFileName(e.target.value)} 
                        />
                        <label htmlFor="username">Nombre del archivo</label>
                    </span>
        
                    <Button 
                        label='Guardar código' 
                        className='p-button-rounded mt-4 p-button-success mb-4' 
                        onClick={ onSave }
                    />               
                </>
            }
        </div>
    )
}

Options.propTypes = {
    setProgram: PropTypes.func.isRequired,
    onCompile: PropTypes.func.isRequired
}


