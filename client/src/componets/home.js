import * as React from 'react';
import PropTypes from 'prop-types';
import Box from '@mui/material/Box';
import EditIcon from '@mui/icons-material/Edit';
import DeleteIcon from '@mui/icons-material/DeleteOutlined';
import SaveIcon from '@mui/icons-material/Save';
import CancelIcon from '@mui/icons-material/Close';
import {
  GridRowModes,
  DataGridPro,
  GridToolbarContainer,
  GridActionsCellItem,
} from '@mui/x-data-grid-pro';

const initialRows = [
  {
    id: 1,
    "ClaimID": 2010,
    "InsuranceID": 1009,
    "FirstName": "Martin",
    "LastName": "Ong",
    "ExpenseDate": "2022-07-14T08:00:00+08:00",
    "Amount": 100.00,
    "Purpose": "Dentist",
    "FollowUp": 0,
    "PreviousClaimID": null,
    "Status": "Approved",
    "LastEditedClaimDate": "2022-07-15T12:22:45+08:00"
   },
   {
    id: 2,
    "ClaimID": 2011,
    "InsuranceID": 1008,
    "FirstName": "John",
    "LastName": "Tan",
    "ExpenseDate": "2022-08-15T08:00:00+08:00",
    "Amount": 100.00,
    "Purpose": "Outpatient Claim",
    "FollowUp": 0,
    "PreviousClaimID": null,
    "Status": "Approved",
    "LastEditedClaimDate": "2022-08-16T19:35:53+08:00"
   },
   {
    id: 3,
    "ClaimID": 2012,
    "InsuranceID": 1005,
    "FirstName": "Mary",
    "LastName": "Lee",
    "ExpenseDate": "2022-08-16T08:00:00+08:00",
    "Amount": 200.00,
    "Purpose": "Specialist Visit",
    "FollowUp": 0,
    "PreviousClaimID": null,
    "Status": "Approved",
    "LastEditedClaimDate": "2022-08-17T12:28:46+08:00"
   },
   {
    id: 4,
    "ClaimID": 2013,
    "InsuranceID": 1007,
    "FirstName": "Mary",
    "LastName": "Lee",
    "ExpenseDate": "2022-08-18T08:00:00+08:00",
    "Amount": 5000.00,
    "Purpose": "Car Repairs",
    "FollowUp": 0,
    "PreviousClaimID": null,
    "Status": "Approved",
    "LastEditedClaimDate": "2022-08-19T11:16:32+08:00"
   },
   {
    id: 5,
    "ClaimID": 2014,
    "InsuranceID": 1008,
    "FirstName": "John",
    "LastName": "Tan",
    "ExpenseDate": "2022-08-20T08:00:00+08:00",
    "Amount": 100.00,
    "Purpose": "Outpatient Claim",
    "FollowUp": 0,
    "PreviousClaimID": null,
    "Status": "Approved",
    "LastEditedClaimDate": "2022-08-29T16:42:51+08:00"
   },
   {
    id: 6,
    "ClaimID": 2015,
    "InsuranceID": 1009,
    "FirstName": "Martin",
    "LastName": "Ong",
    "ExpenseDate": "2022-09-02T08:00:00+08:00",
    "Amount": 100.00,
    "Purpose": "Outpatient Claim",
    "FollowUp": 0,
    "PreviousClaimID": null,
    "Status": "Rejected",
    "LastEditedClaimDate": "2022-09-03T10:30:00+08:00"
   },
   {
    id: 7,
    "ClaimID": 2016,
    "InsuranceID": 1008,
    "FirstName": "John",
    "LastName": "Tan",
    "ExpenseDate": "2022-09-04T08:00:00+08:00",
    "Amount": 100.00,
    "Purpose": "Outpatient Claim",
    "FollowUp": 0,
    "PreviousClaimID": null,
    "Status": "Rejected",
    "LastEditedClaimDate": "2022-09-05T13:25:29+08:00"
   },
   {
    id: 8,
    "ClaimID": 2017,
    "InsuranceID": 1005,
    "FirstName": "Mary",
    "LastName": "Lee",
    "ExpenseDate": "2022-10-08T08:00:00+08:00",
    "Amount": 200.00,
    "Purpose": "Specialist Visit Follow Up",
    "FollowUp": 1,
    "PreviousClaimID": 2013,
    "Status": "Approved",
    "LastEditedClaimDate": "2022-10-09T13:08:24+08:00"
   },
   {
    id: 9,
    "ClaimID": 2018,
    "InsuranceID": 1011,
    "FirstName": "John",
    "LastName": "Tan",
    "ExpenseDate": "2022-10-10T08:00:00+08:00",
    "Amount": 3000.00,
    "Purpose": "Aircon Repair",
    "FollowUp": 0,
    "PreviousClaimID": null,
    "Status": "Pending",
    "LastEditedClaimDate": "2022-10-15T17:45:52+08:00"
   },
   {
    id: 10,
    "ClaimID": 2019,
    "InsuranceID": 1009,
    "FirstName": "Martin",
    "LastName": "Ong",
    "ExpenseDate": "2022-10-26T08:00:00+08:00",
    "Amount": 100.00,
    "Purpose": "Dentist",
    "FollowUp": 0,
    "PreviousClaimID": null,
    "Status": "Approved",
    "LastEditedClaimDate": "2022-10-28T13:08:24+08:00"
   },
   {
    id: 11,
    "ClaimID": 2020,
    "InsuranceID": 1009,
    "FirstName": "Martin",
    "LastName": "Ong",
    "ExpenseDate": "2023-01-03T08:00:00+08:00",
    "Amount": 100.00,
    "Purpose": "Outpatient Claim",
    "FollowUp": 0,
    "PreviousClaimID": null,
    "Status": "Approved",
    "LastEditedClaimDate": "2023-01-05T12:53:04+08:00"
   },
   {
    id: 12,
    "ClaimID": 2021,
    "InsuranceID": 1011,
    "FirstName": "John",
    "LastName": "Tan",
    "ExpenseDate": "2022-12-20T08:00:00+08:00",
    "Amount": 2000.00,
    "Purpose": "Engine Repair",
    "FollowUp": 0,
    "PreviousClaimID": null,
    "Status": "Approved",
    "LastEditedClaimDate": "2023-01-06T11:24:32+08:00"
   },
   {
    id: 13,
    "ClaimID": 2022,
    "InsuranceID": 1005,
    "FirstName": "Mary",
    "LastName": "Lee",
    "ExpenseDate": "2023-01-09T08:00:00+08:00",
    "Amount": 200.00,
    "Purpose": "Specialist Visit Follow Up",
    "FollowUp": 1,
    "PreviousClaimID": 2017,
    "Status": "Approved",
    "LastEditedClaimDate": "2023-01-09T17:23:56+08:00"
   },
   {
    id: 14,
    "ClaimID": 2023,
    "InsuranceID": 1016,
    "FirstName": "Irene",
    "LastName": "Lim",
    "ExpenseDate": "2023-02-11T08:00:00+08:00",
    "Amount": 100.00,
    "Purpose": "Overseas Injury",
    "FollowUp": 0,
    "PreviousClaimID": null,
    "Status": "Approved",
    "LastEditedClaimDate": "2023-02-16T15:32:24+08:00"
   },
   {
    id: 15,
    "ClaimID": 2024,
    "InsuranceID": 1009,
    "FirstName": "Martin",
    "LastName": "Ong",
    "ExpenseDate": "2023-02-23T08:00:00+08:00",
    "Amount": 100.00,
    "Purpose": "Dentist",
    "FollowUp": 0,
    "PreviousClaimID": null,
    "Status": "Pending",
    "LastEditedClaimDate": "2023-02-25T17:33:58+08:00"
   },
   {
    id: 16,
    "ClaimID": 2027,
    "InsuranceID": 1016,
    "FirstName": "Irene",
    "LastName": "Lim",
    "ExpenseDate": "2023-02-11T08:00:00+08:00",
    "Amount": 200.00,
    "Purpose": "Lost Baggage",
    "FollowUp": 0,
    "PreviousClaimID": null,
    "Status": "Pending",
    "LastEditedClaimDate": "2023-02-25T17:39:42+08:00"
   },
   {
    id: 17,
    "ClaimID": 2028,
    "InsuranceID": 1016,
    "FirstName": "Irene",
    "LastName": "Lim",
    "ExpenseDate": "2023-02-28T08:00:00+08:00",
    "Amount": 50.00,
    "Purpose": "Overseas Injury Follow Up Treatment",
    "FollowUp": 1,
    "PreviousClaimID": 2023,
    "Status": "Pending",
    "LastEditedClaimDate": "2023-02-28T17:33:58+08:00"
   },
   {
    id: 18,
    "ClaimID": 2025,
    "InsuranceID": 1015,
    "FirstName": "Sean",
    "LastName": "Chia",
    "ExpenseDate": "2023-02-28T08:00:00+08:00",
    "Amount": 10000.00,
    "Purpose": "Repairs Due to Fire From Neighbor",
    "FollowUp": 0,
    "PreviousClaimID": null,
    "Status": "Pending",
    "LastEditedClaimDate": "2023-03-01T10:00:00+08:00"
   },
   {
    id: 19,
    "ClaimID": 2026,
    "InsuranceID": 1009,
    "FirstName": "Martin",
    "LastName": "Ong",
    "ExpenseDate": "2023-03-10T08:00:00+08:00",
    "Amount": 100.00,
    "Purpose": "Outpatient Claim",
    "FollowUp": 0,
    "PreviousClaimID": null,
    "Status": "Approved",
    "LastEditedClaimDate": "2023-03-11T00:00:00+08:00"
   }
];

function EditToolbar(props) {
  const { setRows, setRowModesModel } = props;



  return (
    <GridToolbarContainer>
    </GridToolbarContainer>
  );
}

EditToolbar.propTypes = {
  setRowModesModel: PropTypes.func.isRequired,
  setRows: PropTypes.func.isRequired,
};

export default function Home() {
  const [rows, setRows] = React.useState(initialRows);
  const [rowModesModel, setRowModesModel] = React.useState({});

  const handleRowEditStart = (params, event) => {
    event.defaultMuiPrevented = true;
  };

  const handleRowEditStop = (params, event) => {
    event.defaultMuiPrevented = true;
  };

  const handleEditClick = (id) => () => {
    setRowModesModel({ ...rowModesModel, [id]: { mode: GridRowModes.Edit } });
  };

  const handleSaveClick = (id) => () => {
    setRowModesModel({ ...rowModesModel, [id]: { mode: GridRowModes.View } });
  };

  const handleDeleteClick = (id) => () => {
    setRows(rows.filter((row) => row.id !== id));
  };

  const handleCancelClick = (id) => () => {
    setRowModesModel({
      ...rowModesModel,
      [id]: { mode: GridRowModes.View, ignoreModifications: true },
    });

    const editedRow = rows.find((row) => row.id === id);
    if (editedRow.isNew) {
      setRows(rows.filter((row) => row.id !== id));
    }
  };

  const processRowUpdate = (newRow) => {
    const updatedRow = { ...newRow, isNew: false };
    setRows(rows.map((row) => (row.id === newRow.id ? updatedRow : row)));
    return updatedRow;
  };

  const columns = [
    { field: 'ClaimID', headerName: 'Claim ID',  editable: false},
    { field: 'InsuranceID', headerName: 'Insurance ID', editable: false },
    { field: 'FirstName', headerName: 'First Name', width:150, editable: false },
    { field: 'LastName', headerName: 'Last Name', width:150, editable: false },
    {
      field: 'ExpenseDate',
      headerName: 'Expense Date',
      type: 'date',
      width: 180,
      editable: false,
    },
    {
      field: 'Amount',
      headerName: 'Amount/$',
      type: 'number',
      width: 180,
      editable: true,
    },
    {
      field: 'Purpose',
      headerName: 'Purpose',
      width: 180,
      editable: true,
    },
    { field: 'FollowUp', headerName: 'Follow Up', type: 'number', editable: true },
    {
      field: 'PreviousClaimID',
      headerName: 'Previous Claim ID',
      width: 180,
      editable: true,
    },
    { field: 'Status', headerName: 'Status', width:150, editable: false },
  
    {
      field: 'LastEditedClaimDate',
      headerName: 'Last Edited Claim Date',
      type: 'dateTime',
      width: 220,
      editable: false,
    },
    {
      field: 'actions',
      type: 'actions',
      headerName: 'Actions',
      width: 100,
      cellClassName: 'actions',
      getActions: ({ id }) => {
        const isInEditMode = rowModesModel[id]?.mode === GridRowModes.Edit;

        if (isInEditMode) {
          return [
            <GridActionsCellItem
              icon={<SaveIcon />}
              label="Save"
              onClick={handleSaveClick(id)}
            />,
            <GridActionsCellItem
              icon={<CancelIcon />}
              label="Cancel"
              className="textPrimary"
              onClick={handleCancelClick(id)}
              color="inherit"
            />,
          ];
        }

        return [
          <GridActionsCellItem
            icon={<EditIcon />}
            label="Edit"
            className="textPrimary"
            onClick={handleEditClick(id)}
            color="inherit"
          />,
          <GridActionsCellItem
            icon={<DeleteIcon />}
            label="Delete"
            onClick={handleDeleteClick(id)}
            color="inherit"
          />,
        ];
      },
    },
  ];

  return (
    <Box
      sx={{
        height: 1000,
        width: '100%',
        '& .actions': {
          color: 'text.secondary',
        },
        '& .textPrimary': {
          color: 'text.primary',
        },
      }}
    >
      <DataGridPro
        rows={rows}
        columns={columns}
        editMode="row"
        rowModesModel={rowModesModel}
        onRowModesModelChange={(newModel) => setRowModesModel(newModel)}
        onRowEditStart={handleRowEditStart}
        onRowEditStop={handleRowEditStop}
        processRowUpdate={processRowUpdate}
        components={{
          Toolbar: EditToolbar,
        }}
        componentsProps={{
          toolbar: { setRows, setRowModesModel },
        }}
        experimentalFeatures={{ newEditingApi: true }}
      />
    </Box>
  );
}