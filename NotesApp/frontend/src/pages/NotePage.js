import React,{useState,useEffect} from 'react'
import {Link, useParams,useNavigate} from 'react-router-dom';
import {ReactComponent as Arrowleft} from '../assets/arrow-left.svg';

const NotePage = ({match,history}) => {
  
  let noteId = useParams().id;
  let [note,setNote] = useState(null);
  const navigate = useNavigate();
  useEffect(()=>{
    getNote();
  },[]);

  let getNote = async ()=>{
    if (noteId === 'new') return
    let response = await fetch(`/api/notes/${noteId}`);
    let data = await response.json();
    setNote(data);
  }

  let updateNote = async()=>{
    fetch(`/api/notes/${noteId}/`,{
      method:'PUT',
      headers:{
        'Content-Type':'application/json'
      },
      body: JSON.stringify(note)
    });
    navigate('/')
  }

  let handleSubmit = () =>{
    if(noteId !== 'new' && note.body===''){
      deleteNote();
    }else if(noteId !== 'new'){
      updateNote();
    }else if(noteId === 'new' && note!==null){
      createNote();
    }
  }

  let deleteNote = async()=>{
    fetch(`/api/notes/${noteId}/`,{
      method:'DELETE',
      'headers':{
        'Content-Type': 'application/json'
      }
    });
    navigate('/');
  }

  let createNote = async()=>{
    fetch(`/api/notes/`,{
      method:'POST',
      'headers':{
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(note)
    });
    navigate('/');
  }
  
  
  

  return (
    <div className='note'>
      <div className='note-header'>
        <h3>
          <Arrowleft onClick={handleSubmit}/>
                  
        </h3>
        {noteId!=='new'?(
            <button onClick={deleteNote}>Delete</button>
        ):(
            <button onClick={handleSubmit}>Save</button>
        )}
         
      </div>
        <textarea onChange={(e)=>setNote({...note, 'body':e.target.value})} value={note?.body}></textarea>
    </div>
  )
}

export default NotePage