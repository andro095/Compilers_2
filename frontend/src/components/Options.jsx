import PropTypes from 'prop-types';

import { FileUpload } from 'primereact/fileupload';
import { Button } from 'primereact/button';

export const Options = ({ setProgram, onExecute }) => {

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
                label='Ejecutar' 
                className='p-button-rounded mt-4 p-button-success mb-4' 
                onClick={ onExecute }
            />               
        </div>
    )
}

Options.propTypes = {
    setProgram: PropTypes.func.isRequired,
    onExecute: PropTypes.func.isRequired
}


