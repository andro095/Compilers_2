import React from 'react'
import PropTypes from 'prop-types'

import { TabView, TabPanel } from 'primereact/tabview';
import Editor from '@monaco-editor/react'

export const MyCodes = ({intercode, obj_code}) => {

  return (
    <div className='w-4 mx-2 mb-2 bg-red-500 border-round overflow-hidden flex flex-column'>
        <TabView className='h-full' panelContainerClassName='h-full'>
            <TabPanel contentClassName='h-full' header="Código intermedio">
                <Editor
                    height="93%"
                    width="100%"
                    defaultValue="-- Aqui aparece el codigo intermedio"
                    className='shadow-4'
                    value={ intercode }
                    options={{readOnly: true}}
                />
            </TabPanel>
            <TabPanel contentClassName='h-full' header="Código ensamblador">
                <Editor
                    height="93%"
                    width="100%"
                    defaultValue="-- Aqui aparece el codigo ensamblador"
                    className='shadow-4'
                    value={ obj_code }
                    options={{readOnly: true}}
                />
            </TabPanel>
        </TabView>
        
    </div>
  )
}

MyCodes.propTypes = {
    intercode: PropTypes.string.isRequired,
    obj_code: PropTypes.string.isRequired
}

