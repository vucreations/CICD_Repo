import {render, screen} from '@testing-library/react'
import HelloWorld from '.'


it("should have hello world", ()=>{
    render(<HelloWorld />)
    const message = screen.queryByText(/Hello world/i)
    expect(message).toBeVisible()
})


it("should not have random text", ()=>{
    render(<HelloWorld />)
    const message = screen.queryByText("Random")
    expect(message).not.toBeInTheDocument()
})