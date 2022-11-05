import { useState } from "react";

export const useSave = () => {

    const [fileName, setFileName] = useState('');
    
    const onSave = (objCode) => {
        objCode = 'test';
        const url = window.URL.createObjectURL(new Blob([objCode], { type: 'text/plain' }));
        const link = document.createElement('a');
        link.href = url;
        link.setAttribute(
            'download',
            `${fileName}.yapl`,
        );

        // Append to html link element page
        document.body.appendChild(link);

        // Start download
        link.click();

        // Clean up and remove the link
        link.parentNode.removeChild(link);
    }
    
    return {
        onSave,
        setFileName,
        fileName
    }
}
