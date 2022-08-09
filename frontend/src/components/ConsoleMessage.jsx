import React from 'react'
import PropTypes from 'prop-types'

const msgTypes = {
    info: 'text-color',
    error: 'text-red-500',
    warning: 'text-orange-500',
    success: 'text-green-500'
}

export const ConsoleMessage = ({ type = 'info', msg }) => {
    

    return (
        <div className={ msgTypes[type] }>
            <p className='m-0 mb-1'>{ msg }</p>
        </div>
    )
}

ConsoleMessage.propTypes = {
    type: PropTypes.string,
    msg: PropTypes.string.isRequired
}
